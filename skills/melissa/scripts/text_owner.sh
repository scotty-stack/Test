#!/bin/bash
# Text the owner (and only the owner). Every message starts with "Melissa ·" so the
# reply reader can tell Melissa's texts from the owner's in a shared note-to-self thread.
# Usage: text_owner.sh "<message>"
set -euo pipefail
[ $# -eq 1 ] || { echo "usage: $0 \"<message>\"" >&2; exit 1; }
source "$HOME/Melissa/config.sh"

msg="$1"
case "$msg" in
  "Melissa ·"*) ;;
  *) msg="Melissa · $msg" ;;
esac
exec "$(dirname "$0")/send_imessage.sh" "$OWNER_HANDLE" "$msg"
