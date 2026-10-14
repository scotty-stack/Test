#!/bin/bash
# One-time Mac mini setup: Melissa's config and her two scheduled jobs.
# Usage (from the repo root):  skills/melissa/scripts/install.sh +14054201941
# Re-run any time to change the run times; it replaces the jobs, keeps your config.
set -euo pipefail
[ $# -ge 1 ] || { echo "usage: $0 <owner mobile, e.g. +14054201941>" >&2; exit 1; }

scripts="$(cd "$(dirname "$0")" && pwd)"
mkdir -p "$HOME/Melissa" "$HOME/Library/LaunchAgents"
claude_bin="$(command -v claude || true)"
[ -n "$claude_bin" ] || { echo "Install Claude Code first (claude not found on PATH)" >&2; exit 1; }

cfg="$HOME/Melissa/config.sh"
if [ ! -f "$cfg" ]; then
  cat > "$cfg" <<CFG
# Melissa's settings on this Mac. Not in the repo; keep keys and numbers here.
OWNER_HANDLE="$1"
SELF_MODE=1                 # 1 = Messages on this Mac uses the owner's Apple ID
CLAUDE_BIN="$claude_bin"
# Tool name prefixes for the Google connectors. Check with: claude mcp list
GMAIL_MCP="mcp__claude_ai_Gmail"
SHEETS_MCP="mcp__claude_ai_Google_Sheets"
DRIVE_MCP="mcp__claude_ai_Google_Drive"
MLS_API_HOST=""             # set when the MLS API is approved, e.g. api-trestle.corelogic.com
SEARCH_HOURS="8 12 17"      # scheduled search times (24h)
CFG
  echo "wrote $cfg"
fi
source "$cfg"

path="$(dirname "$claude_bin"):/usr/local/bin:/opt/homebrew/bin:/usr/bin:/bin"

times=""
for h in $SEARCH_HOURS; do
  times+="<dict><key>Hour</key><integer>$h</integer><key>Minute</key><integer>5</integer></dict>"
done

write_job() {  # label, script, schedule xml
  local plist="$HOME/Library/LaunchAgents/$1.plist"
  cat > "$plist" <<PLIST
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>$1</string>
  <key>ProgramArguments</key><array><string>$scripts/$2</string></array>
  <key>EnvironmentVariables</key><dict><key>PATH</key><string>$path</string></dict>
  $3
  <key>StandardOutPath</key><string>$HOME/Melissa/launchd.log</string>
  <key>StandardErrorPath</key><string>$HOME/Melissa/launchd.log</string>
</dict></plist>
PLIST
  launchctl bootout "gui/$(id -u)/$1" 2>/dev/null || true
  launchctl bootstrap "gui/$(id -u)" "$plist"
  echo "scheduled $1"
}

write_job com.melissa.search run_search.sh "<key>StartCalendarInterval</key><array>$times</array>"
write_job com.melissa.replies watch_replies.sh "<key>StartInterval</key><integer>120</integer>"

# Start the reply reader from "now" so old texts aren't treated as replies.
python3 -I "$scripts/read_replies.py" >/dev/null && echo "reply reader ready"
echo "Done. Log: ~/Melissa/melissa.log   Stop everything: $scripts/uninstall.sh"
