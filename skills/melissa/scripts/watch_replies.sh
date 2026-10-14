#!/bin/bash
# Runs every 2 minutes (launchd). Cheap: wakes Claude only when the owner has texted.
set -euo pipefail
dir="$(dirname "$0")"
n=$(python3 -I "$dir/read_replies.py" --watch)
[ "$n" = "0" ] && exit 0
exec "$dir/melissa_claude.sh" "Melissa: the owner texted you. Run Step 5 of the melissa skill."
