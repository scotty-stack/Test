#!/bin/bash
# Runs every 2 minutes from launchd. Cheap: only wakes Claude when the owner has texted.
set -euo pipefail
cd "$(dirname "$0")/../../.."          # repo root, where Claude Code finds the skill
source "$HOME/Melissa/config.sh"       # OWNER_HANDLE, SELF_MODE

flags=(--from "$OWNER_HANDLE" --peek)
[ "${SELF_MODE:-0}" = "1" ] && flags+=(--self)

new=$(python3 -I skills/melissa/scripts/read_replies.py "${flags[@]}")
[ "$new" = "[]" ] && exit 0

claude -p "Melissa: the owner replied by text. Run Step 5 of the melissa skill." \
  --allowedTools "Bash(python3 -I skills/melissa/scripts/*),Bash(skills/melissa/scripts/send_imessage.sh *),Read" \
  >> "$HOME/Melissa/melissa.log" 2>&1
