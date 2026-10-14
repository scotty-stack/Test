#!/usr/bin/env python3
"""Text the owner a shortlist and remember it, so "SEND Smiths 1 3" maps to the right homes.

Usage:
  python3 -I skills/melissa/scripts/shortlist.py add < shortlist.json   # text it to the owner, save it
  python3 -I skills/melissa/scripts/shortlist.py add --dry-run < ...    # print the text, send nothing
  python3 -I skills/melissa/scripts/shortlist.py show [--buyer Smiths]  # latest open shortlist
  python3 -I skills/melissa/scripts/shortlist.py open                   # every open shortlist
  python3 -I skills/melissa/scripts/shortlist.py more <id>              # text the owner the next 5
  python3 -I skills/melissa/scripts/shortlist.py close <id> [--status sent|skipped|mixed]

shortlist.json:
  {"buyer": "Smiths", "search": "Edmond · $350–425k",
   "to": [{"name": "Jen", "handle": "+14055551234"}],          # from the buyer sheet; add "sms": true for Android
   "items": [{"address": "1412 Elm Ct", "price": 399000, "price_drop": 0,
              "beds": 4, "baths": 2, "sqft": 2140,
              "fit": "Deer Creek schools, no HOA, fenced yard",
              "watch": "Backs to Memorial Rd, ask about noise",
              "link": "https://...", "mls": "1234567"}]}

The recipients are printed in the owner's text and stored here. send_to_client.py only
ever texts those recipients, so what the owner approves is exactly who gets it.
"""
import argparse
import datetime
import json
import os
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import common  # noqa: E402

PAGE = 5


def money(n):
    n = int(n or 0)
    return f"${n / 1_000_000:.2f}M" if n >= 1_000_000 else f"${round(n / 1000)}k"


def pretty_phone(h):
    d = common.digits(h)
    return f"{d[:3]}-{d[3:6]}-{d[6:]}" if len(d) == 10 else h


def format_text(s, start):
    items = s["items"][start:start + PAGE]
    who = ", ".join(f'{t["name"]} {pretty_phone(t["handle"])}' for t in s["to"])
    lines = [f'{common.MARKER} {s["buyer"]} ({s.get("search", "")}) · {len(s["items"])} new', f"→ goes to {who}", ""]
    for it in items:
        price = money(it["price"])
        if it.get("price_drop"):
            price += f' (↓{money(it["price_drop"])})'
        size = f' · {it["sqft"]:,}sf' if it.get("sqft") else ""
        lines += [
            f'{it["n"]}) {it["address"]} · {price} · {it.get("beds", "?")}/{it.get("baths", "?")}{size}',
            f'   ✅ {it.get("fit") or "—"}',
            f'   ⚠️ {it.get("watch") or "Nothing jumped out"}',
            f'   {it["link"]}',
            "",
        ]
    rest = len(s["items"]) - (start + len(items))
    if rest > 0:
        lines.append(f"+{rest} more, reply MORE {s['buyer']}")
    b = s["buyer"]
    lines.append(f"Reply: SEND {b} 1 2 · SEND {b} (all) · SKIP {b} 2 <why> · EDIT {b} 2 <note>")
    return "\n".join(lines)


def text_owner(msg, dry):
    if dry:
        print(msg)
        return
    subprocess.run([os.path.join(common.SCRIPTS, "text_owner.sh"), msg], check=True)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    add = sub.add_parser("add")
    add.add_argument("--dry-run", action="store_true")
    show = sub.add_parser("show")
    show.add_argument("--buyer")
    sub.add_parser("open")
    more = sub.add_parser("more")
    more.add_argument("id")
    more.add_argument("--dry-run", action="store_true")
    close = sub.add_parser("close")
    close.add_argument("id")
    close.add_argument("--status", default="closed")
    args = ap.parse_args()

    data = common.load_json(common.SHORTLISTS, [])

    if args.cmd == "add":
        s = json.load(sys.stdin)
        if not s.get("buyer") or not s.get("items") or not s.get("to"):
            sys.exit("shortlist needs buyer, to, and items")
        for t in s["to"]:
            if len(common.digits(t.get("handle", ""))) < 10 and "@" not in t.get("handle", ""):
                sys.exit(f"bad recipient handle: {t}")
        for i, it in enumerate(s["items"], 1):
            if not it.get("link") or not it.get("address"):
                sys.exit(f"item {i} needs address and link")
            it["n"] = i
        now = datetime.datetime.now().astimezone()
        s.update(id=now.strftime("%Y%m%d%H%M%S"), created=now.isoformat(timespec="seconds"),
                 status="open", shown=min(PAGE, len(s["items"])))
        text_owner(format_text(s, 0), args.dry_run)
        if not args.dry_run:
            # Remove shortlists older than 30 days so the file stays small.
            cutoff = (now - datetime.timedelta(days=30)).isoformat()
            data = [x for x in data if x["created"] >= cutoff] + [s]
            common.save_json(common.SHORTLISTS, data)
        print(s["id"])

    elif args.cmd in ("show", "open"):
        found = [s for s in data if s["status"] == "open"
                 and (args.cmd == "open" or not args.buyer or s["buyer"].lower() == args.buyer.lower())]
        json.dump(found if args.cmd == "open" else (found[-1] if found else None),
                  sys.stdout, indent=2, ensure_ascii=False)
        print()

    elif args.cmd == "more":
        s = next((x for x in data if x["id"] == args.id), None) or sys.exit("no such shortlist")
        if s["shown"] >= len(s["items"]):
            sys.exit("nothing more in this shortlist")
        text_owner(format_text(s, s["shown"]), args.dry_run)
        if not args.dry_run:
            s["shown"] = min(s["shown"] + PAGE, len(s["items"]))
            common.save_json(common.SHORTLISTS, data)

    elif args.cmd == "close":
        for s in data:
            if s["id"] == args.id:
                s["status"] = args.status
        common.save_json(common.SHORTLISTS, data)


if __name__ == "__main__":
    main()
