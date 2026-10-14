#!/bin/bash
# Start Claude Code headless as Melissa, with only Melissa's tools. Used by the scheduled
# jobs. Anything not listed here is refused when nobody is watching: she can read Gmail,
# read/write her buyer sheet, find it in Drive, and run her own scripts. She cannot send
# email, delete or share files, or run any other command.
# Usage: melissa_claude.sh "<prompt>"
set -euo pipefail
cd "$(dirname "$0")/../../.."                 # repo root, where Claude Code finds the skill
source "$HOME/Melissa/config.sh"

# Run one at a time; a run still going means skip this one.
lock="$HOME/Melissa/run.lock"
if ! mkdir "$lock" 2>/dev/null; then
  if [ -n "$(find "$lock" -maxdepth 0 -mmin +30)" ]; then rmdir "$lock" && mkdir "$lock"; else exit 0; fi
fi
trap 'rmdir "$lock"' EXIT

S="skills/melissa/scripts"
allowed=(
  "Read"
  "Bash(python3 -I $S/read_replies.py:*)"
  "Bash(python3 -I $S/shortlist.py:*)"
  "Bash(python3 -I $S/send_to_client.py:*)"
  "Bash($S/text_owner.sh:*)"
  "${GMAIL_MCP}__search_threads" "${GMAIL_MCP}__get_thread" "${GMAIL_MCP}__get_message"
  "${SHEETS_MCP}__get_spreadsheet" "${SHEETS_MCP}__get_values"
  "${SHEETS_MCP}__update_values" "${SHEETS_MCP}__append_values"
  "${DRIVE_MCP}__search_files"
)
[ -n "${MLS_API_HOST:-}" ] && allowed+=("WebFetch(domain:$MLS_API_HOST)")

echo "=== $(date '+%F %T') $1" >> "$HOME/Melissa/melissa.log"
"$CLAUDE_BIN" -p "$1" --allowedTools "${allowed[@]}" >> "$HOME/Melissa/melissa.log" 2>&1
