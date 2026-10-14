#!/usr/bin/env python3
"""Remember the shortlists Melissa texted the owner, so "SEND 1 3" maps to the right homes.

Usage:
  python3 -I pending.py add < shortlist.json     # save a shortlist Melissa just texted
  python3 -I pending.py show                     # most recent open shortlist
  python3 -I pending.py show --buyer Smiths      # most recent open shortlist for a buyer
  python3 -I pending.py open                     # every open shortlist
  python3 -I pending.py close <id>               # done (sent / skipped)

shortlist.json:
  {"buyer": "Smiths", "items": [
     {"n": 1, "address": "1412 Elm Ct", "price": 399000, "link": "https://...", "mls": "1234567"}
  ]}
"""
import argparse
import datetime
import json
import os
import sys

FILE = os.path.expanduser("~/Melissa/pending.json")
KEEP_DAYS = 14


def load():
    try:
        with open(FILE) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save(data):
    os.makedirs(os.path.dirname(FILE), exist_ok=True)
    cutoff = (datetime.datetime.now() - datetime.timedelta(days=KEEP_DAYS)).isoformat()
    data = [s for s in data if s["created"] >= cutoff]
    tmp = FILE + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, FILE)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("add")
    show = sub.add_parser("show")
    show.add_argument("--buyer")
    sub.add_parser("open")
    close = sub.add_parser("close")
    close.add_argument("id")
    args = ap.parse_args()

    data = load()
    if args.cmd == "add":
        s = json.load(sys.stdin)
        if not s.get("buyer") or not s.get("items"):
            sys.exit("shortlist needs a buyer and items")
        now = datetime.datetime.now()
        s.update(id=now.strftime("%Y%m%d%H%M%S"), created=now.isoformat(), status="open")
        data.append(s)
        save(data)
        print(s["id"])
    elif args.cmd in ("show", "open"):
        found = [s for s in data if s["status"] == "open"
                 and (args.cmd == "open" or not args.buyer or s["buyer"].lower() == args.buyer.lower())]
        result = found if args.cmd == "open" else (found[-1] if found else None)
        json.dump(result, sys.stdout, indent=2, ensure_ascii=False)
        print()
    elif args.cmd == "close":
        for s in data:
            if s["id"] == args.id:
                s["status"] = "closed"
        save(data)


if __name__ == "__main__":
    main()
