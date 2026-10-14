#!/usr/bin/env python3
"""Text a client listings the owner approved. The only way Melissa can text a client.

Usage:
  python3 -I skills/melissa/scripts/send_to_client.py --shortlist <id> --items 1,3 \
      --reply-id <id from read_replies.py> --message "Hey Jen! ... https://..."

Refuses to send unless ALL of these hold:
  1. The shortlist exists and is open.
  2. --reply-id is a real text from the owner in Messages, sent after the shortlist.
  3. That text approves (SEND / YES / OK / APPROVE / EDIT), and if numbers follow the
     word, every --items number is among them. No numbers means all.
  4. If more than one shortlist was open when the owner replied, the reply names this
     shortlist's buyer.
  5. Every link in --message belongs to an approved item, and there is at least one.
  6. None of these items already went to this buyer.
Recipients come from the shortlist (shown to the owner in the shortlist text), never
from the command line.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

APPROVE = re.compile(r"^\s*(send|yes|yep|yeah|ok|okay|approve|approved|edit|go)\b", re.I)


def fail(msg):
    print(f"NOT SENT: {msg}", file=sys.stderr)
    sys.exit(2)


def approved_numbers(text, buyer):
    """Numbers right after the verb (and optional buyer name): 'SEND Smiths 1, 3 & 4' -> {1,3,4}.
    Numbers later in the text (an EDIT note's '30x40 shop') don't count. None means all."""
    rest = APPROVE.sub("", text, count=1)
    rest = re.sub(r"^\s*" + re.escape(buyer) + r"\b", "", rest, flags=re.I)
    m = re.match(r"^[\s#:,-]*((?:\d+(?:\s*(?:,|&|and|\s)\s*)?)+)", rest, re.I)
    return {int(n) for n in re.findall(r"\d+", m.group(1))} if m else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shortlist", required=True)
    ap.add_argument("--items", required=True, help="comma-separated item numbers, e.g. 1,3")
    ap.add_argument("--reply-id", required=True, type=int)
    ap.add_argument("--message", required=True)
    ap.add_argument("--dry-run", action="store_true", help="run every check, send nothing")
    args = ap.parse_args()

    cfg = common.config()
    data = common.load_json(common.SHORTLISTS, [])
    s = next((x for x in data if x["id"] == args.shortlist), None)
    if not s or s["status"] != "open":
        fail("no open shortlist with that id")
    try:
        want = {int(n) for n in args.items.split(",") if n.strip()}
    except ValueError:
        fail("--items must be numbers like 1,3")
    items = {it["n"]: it for it in s["items"]}
    if not want or not want <= items.keys():
        fail(f"items {sorted(want)} not in shortlist (has {sorted(items)})")

    # 2. A real owner text, after the shortlist went out.
    replies = common.owner_messages(common.connect(), cfg, rowid=args.reply_id)
    if not replies:
        fail(f"message {args.reply_id} is not a text from the owner")
    reply = replies[0]
    if datetime.datetime.fromisoformat(reply["time"]) < datetime.datetime.fromisoformat(s["created"]).replace(second=0):
        fail("that reply was sent before this shortlist")

    # 3. It approves these items.
    if not APPROVE.match(reply["text"]):
        fail(f'reply "{reply["text"]}" is not an approval (SEND / YES / OK / EDIT)')
    nums = approved_numbers(reply["text"], s["buyer"])
    if nums is not None and not want <= nums:
        fail(f'reply "{reply["text"]}" approves {sorted(nums)}, not {sorted(want)}')

    # 4. Unambiguous when several shortlists were waiting.
    reply_time = datetime.datetime.fromisoformat(reply["time"])
    rivals = [x for x in data if x["id"] != s["id"] and x["status"] == "open"
              and datetime.datetime.fromisoformat(x["created"]).replace(second=0) <= reply_time]
    if rivals and s["buyer"].lower() not in reply["text"].lower():
        fail(f'{len(rivals) + 1} shortlists were open and the reply doesn\'t name "{s["buyer"]}"; ask the owner which buyer')

    # 5. Links in the message are only the approved listings.
    links = re.findall(r"https?://\S+", args.message)
    allowed = {items[n]["link"].rstrip("/.,") for n in want}
    if not links:
        fail("message has no listing link")
    stray = [u for u in links if u.rstrip("/.,)") not in allowed]
    if stray:
        fail(f"message has links that aren't approved listings: {stray}")

    # 6. Not sent before.
    sent = set()
    if os.path.exists(common.SENT_LOG):
        with open(common.SENT_LOG) as f:
            for line in f:
                e = json.loads(line)
                sent.add((e["buyer"].lower(), e["link"]))
    dupes = [n for n in want if (s["buyer"].lower(), items[n]["link"]) in sent]
    if dupes:
        fail(f"items {dupes} already went to {s['buyer']}")

    if args.dry_run:
        print("checks passed; dry run, nothing sent")
        return

    for t in s["to"]:
        cmd = [os.path.join(common.SCRIPTS, "send_imessage.sh"), t["handle"], args.message]
        if t.get("sms"):
            cmd.append("sms")
        subprocess.run(cmd, check=True)

    now = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    with open(common.SENT_LOG, "a") as f:
        for n in sorted(want):
            f.write(json.dumps({"time": now, "buyer": s["buyer"], "shortlist": s["id"], "n": n,
                                "address": items[n]["address"], "link": items[n]["link"],
                                "reply_id": args.reply_id, "to": [t["handle"] for t in s["to"]]}) + "\n")
    names = ", ".join(t["name"] for t in s["to"])
    print(f"sent {', '.join(items[n]['address'] for n in sorted(want))} to {names}")


if __name__ == "__main__":
    main()
