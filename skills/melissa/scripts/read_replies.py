#!/usr/bin/env python3
"""New texts from the owner to Melissa, as JSON.

Usage:
  python3 -I skills/melissa/scripts/read_replies.py          # new replies, then mark them read
  python3 -I skills/melissa/scripts/read_replies.py --peek   # new replies, leave them unread
  python3 -I skills/melissa/scripts/read_replies.py --watch  # for watch_replies.sh: count of replies
                                                             # it hasn't woken Melissa for yet

Prints: [{"id": 1234, "time": "2026-10-14T12:03-05:00", "text": "SEND 1 3"}, ...]
The "id" is what send_to_client.py needs as --reply-id.

Needs Full Disk Access (see reference/mac-mini-setup.md). Opens the database read-only.
"""
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--peek", action="store_true", help="don't mark messages as read")
    ap.add_argument("--watch", action="store_true", help="print how many replies are new to the watcher")
    args = ap.parse_args()

    cfg = common.config()
    state = common.load_json(common.STATE, {})
    con = common.connect()
    top = common.max_rowid(con)
    last = state.get("last_rowid", top)  # first run starts from now, no replay of history

    if args.watch:
        # Wake Melissa once per new reply, even if her run fails before marking it read,
        # so a broken run can't re-trigger every 2 minutes.
        seen = max(last, state.get("watch_rowid", 0))
        new = common.owner_messages(con, cfg, after_rowid=seen)
        state["watch_rowid"] = top
        state.setdefault("last_rowid", last)
        common.save_json(common.STATE, state)
        print(len(new))
        return

    out = common.owner_messages(con, cfg, after_rowid=last)
    if not args.peek:
        state["last_rowid"] = top
        common.save_json(common.STATE, state)
    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
