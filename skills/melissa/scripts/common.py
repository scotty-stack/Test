"""Shared helpers for Melissa's Mac mini scripts: config, the Messages database, owner texts."""
import datetime
import json
import os
import re
import sqlite3

HOME = os.path.expanduser("~/Melissa")
CONFIG = os.path.join(HOME, "config.sh")
STATE = os.path.join(HOME, "state.json")
SHORTLISTS = os.path.join(HOME, "shortlists.json")
SENT_LOG = os.path.join(HOME, "sent.jsonl")
DB = os.path.expanduser("~/Library/Messages/chat.db")
SCRIPTS = os.path.dirname(os.path.abspath(__file__))
MARKER = "Melissa ·"
APPLE_EPOCH = datetime.datetime(2001, 1, 1, tzinfo=datetime.timezone.utc)


def config():
    """Read KEY="value" lines from ~/Melissa/config.sh (written by install.sh)."""
    cfg = {}
    with open(CONFIG) as f:
        for line in f:
            m = re.match(r'\s*([A-Z_]+)=["\']?([^"\'#\n]*)', line)
            if m:
                cfg[m.group(1)] = m.group(2).strip()
    cfg["SELF_MODE"] = cfg.get("SELF_MODE", "1") == "1"
    return cfg


def digits(handle):
    """Last 10 digits of a phone number, or the lowercased email, so formats compare equal."""
    if "@" in (handle or ""):
        return handle.lower()
    return re.sub(r"\D", "", handle or "")[-10:]


def load_json(path, default):
    try:
        with open(path) as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    tmp = path + ".tmp"
    with open(tmp, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    os.replace(tmp, path)


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


def connect():
    con = sqlite3.connect(f"file:{DB}?mode=ro", uri=True)
    con.row_factory = sqlite3.Row
    return con


def owner_messages(con, cfg, after_rowid=0, rowid=None):
    """Texts the owner wrote to Melissa, newest last.

    SELF_MODE (Mac signed in to the owner's Apple ID): the owner and Melissa share the
    owner's "note to self" thread, where every message counts as "from me"; Melissa's own
    texts always start with MARKER, so anything else in that thread is the owner's.
    Otherwise: messages from the owner's handle that weren't sent by this Mac.
    """
    owner = digits(cfg["OWNER_HANDLE"])
    where, params = ("m.ROWID = ?", (rowid,)) if rowid is not None else ("m.ROWID > ?", (after_rowid,))
    rows = con.execute(
        f"""
        SELECT m.ROWID AS id, m.text, m.attributedBody, m.is_from_me, m.date,
               h.id AS sender, c.chat_identifier AS chat
        FROM message m
        LEFT JOIN handle h ON h.ROWID = m.handle_id
        LEFT JOIN chat_message_join cmj ON cmj.message_id = m.ROWID
        LEFT JOIN chat c ON c.ROWID = cmj.chat_id
        WHERE {where}
        ORDER BY m.ROWID
        """,
        params,
    ).fetchall()
    out = []
    for r in rows:
        text = r["text"] or decode_attributed_body(r["attributedBody"])
        if not text or not text.strip() or text.startswith(MARKER):
            continue
        if cfg["SELF_MODE"]:
            if digits(r["chat"]) != owner:
                continue
        elif r["is_from_me"] or digits(r["sender"]) != owner:
            continue
        when = APPLE_EPOCH + datetime.timedelta(seconds=(r["date"] or 0) / 1e9)
        out.append({"id": r["id"], "time": when.astimezone().isoformat(timespec="minutes"), "text": text.strip()})
    return out


def max_rowid(con):
    return con.execute("SELECT IFNULL(MAX(ROWID), 0) FROM message").fetchone()[0]
