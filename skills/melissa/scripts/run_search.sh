#!/bin/bash
# Scheduled search (launchd, at the run times in install.sh). Steps 2-4 of the skill.
exec "$(dirname "$0")/melissa_claude.sh" \
  "Melissa: scheduled run. Do Steps 2-4 of the melissa skill for every Active buyer. Text the owner only if something new fits or something is waiting on them."
