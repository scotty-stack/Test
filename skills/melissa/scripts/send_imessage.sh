#!/bin/bash
# Send a text through the Mac's Messages app.
# Usage: send_imessage.sh <phone or email> <message> [sms]
#   Phone numbers in +1XXXXXXXXXX form. Pass "sms" as the third argument to send as a
#   green-bubble text (needs Text Message Forwarding from the owner's iPhone).
# The handle and message go in as arguments, never pasted into the script, so quotes
# and apostrophes in a message can't break it.
set -euo pipefail

if [ $# -lt 2 ]; then
  echo "usage: $0 <phone-or-email> <message> [sms]" >&2
  exit 1
fi

service="iMessage"
[ "${3:-}" = "sms" ] && service="SMS"

osascript - "$1" "$2" "$service" <<'APPLESCRIPT'
on run argv
  set theHandle to item 1 of argv
  set theText to item 2 of argv
  set theService to item 3 of argv
  tell application "Messages"
    if theService is "SMS" then
      set svc to 1st account whose service type = SMS
    else
      set svc to 1st account whose service type = iMessage
    end if
    set who to participant theHandle of svc
    send theText to who
  end tell
end run
APPLESCRIPT

echo "sent via $service to $1"
