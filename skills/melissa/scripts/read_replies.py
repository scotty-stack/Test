#!/usr/bin/env python3
"""Read new texts from the owner out of the Mac's Messages database.

Usage:
  python3 -I read_replies.py --from +14055551234            # new replies, then mark them read
  python3 -I read_replies.py --from +14055551234 --peek     # new replies, leave them unread
  python3 -I read_replies.py --from +14055551234 --self     # Mac signed in to the owner's own Apple ID

Prints JSON: [{"id": 1234, "time": "2026-10-14 12:03", "text": "SEND 1 3"}, ...]

Needs Full Disk Access for the app running it (Terminal, or the launchd job's shell);
see reference/mac-mini-setup.md. Opens the database read-only.

--self: when the Mac uses the owner's Apple ID, Melissa and the owner share one
"note to self" thread. Every message there counts as "from me", so Melissa's own texts
are told apart by the "Melissa ·" prefix she always starts with.
"""
import argparse
import datetime
import json
import os
import re
import sqlite3
import sys

DB = os.path.expanduser("~/Library/Messages/chat.db")
STATE = os.path.expanduser("~/Melissa/state.json")
MARKER = "Melissa ·"
APPLE_EPOCH = datetime.datetime(2001, 1, 1)


def digits(handle):
    """Last 10 digits of a phone number, or the lowercased email."""
    if "@" in handle:
        return handle.lower()
    d = re.sub(r"\D", "", handle)
    return d[-10:]


def decode_attributed_body(blob):
    """Newer macOS leaves message.text empty and stores the text in attributedBody."""
    if not blob:
        return None
    try:
        start = blob.index(b"NSString") + len(b"NSString") + 5
        b = blob[start:]
        length, offset = b[0], 1
        if length == 0x81:
            length, offset = int.from_bytes(b[1:3], "little"), 3
        elif length == 0x82:
            length, offset = int.from_bytes(b[1:4], "little"), 4
        return b[offset:offset + length].decode("utf-8", "replace")
    except (ValueError, IndexError):
        return None


def load_state():
    try:
        with open(STATE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state):
    os.makedirs(os.path.dirname(STATE), exist_ok=True)
    tmp = STATE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(state, f, indent=2)
    os.replace(tmp, STATE)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--from", dest="owner", required=True, help="owner's phone or Apple ID email")
    ap.add_argument("--peek", action="store_true", help="don't mark messages as read")
    ap.add_argument("--self", dest="self_mode", action="store_true", help="Mac uses the owner's Apple ID")
    args = ap.parse_args()

    state = load_state()
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row

    last = state.get("last_rowid")
    if last is None:
        # First run: start from now, don't replay old history.
        last = con.execute("SELECT IFNULL(MAX(ROWID), 0) FROM message").fetchone()[0]

    rows = con.execute(
        """
        SELECT m.ROWID AS id, m.text, m.attributedBody, m.is_from_me, m.date,
               h.id AS sender, c.chat_identifier AS chat
        FROM message m
        LEFT JOIN handle h ON h.ROWID = m.handle_id
        LEFT JOIN chat_message_join cmj ON cmj.message_id = m.ROWID
        LEFT JOIN chat c ON c.ROWID = cmj.chat_id
        WHERE m.ROWID > ?
        ORDER BY m.ROWID
        """,
        (last,),
    ).fetchall()

    owner = digits(args.owner)
    out, max_id = [], last
    for r in rows:
        max_id = max(max_id, r["id"])
        text = r["text"] or decode_attributed_body(r["attributedBody"])
        if not text or not text.strip():
            continue
        if args.self_mode:
            if digits(r["chat"] or "") != owner or text.startswith(MARKER):
                continue
        else:
            if r["is_from_me"] or digits(r["sender"] or "") != owner:
                continue
        when = APPLE_EPOCH + datetime.timedelta(seconds=(r["date"] or 0) / 1e9)
        when = when.replace(tzinfo=datetime.timezone.utc).astimezone()
        out.append({"id": r["id"], "time": when.strftime("%Y-%m-%d %H:%M"), "text": text.strip()})

    if not args.peek:
        state["last_rowid"] = max_id
        save_state(state)

    json.dump(out, sys.stdout, indent=2, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
