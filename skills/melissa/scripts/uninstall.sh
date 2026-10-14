#!/bin/bash
# Stop Melissa's scheduled jobs. Keeps ~/Melissa (config, logs, sent history).
for job in com.melissa.search com.melissa.replies; do
  launchctl bootout "gui/$(id -u)/$job" 2>/dev/null || true
  rm -f "$HOME/Library/LaunchAgents/$job.plist"
  echo "stopped $job"
done
