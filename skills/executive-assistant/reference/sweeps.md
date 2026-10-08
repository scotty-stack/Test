# Sweeps

Each sweep reads the ledger first and writes it back last.

## Morning sweep (weekdays, around 7:45am)

1. **Calendar**: today's events. For each one with a client, pull that person's People row so Scotty walks in knowing the last touch and open items.
2. **Due today and overdue**: Reminders, Follow-ups, Waiting-on chase dates, and Tasks dated today or earlier.
3. **Going cold**: People rows where `Next touch` has passed, or where an active client or lead has gone past the cold threshold in `ledger-format.md`.
4. **Waiting on a reply from Scotty** (see below).
5. Build **Today**: 5 items max, ranked by money and time pressure. Order: deals under contract with a deadline, then new leads (speed matters), then active clients going cold, then partners and vendors, then admin.
6. Deliver it in chat:

```
Good morning. 3 calls, 2 replies, 1 chase.
TODAY
1. Call Maria Lopez: inspection response due 5pm (under contract)
2. Reply to new Zillow lead Tom Reyes (came in 9:40pm, no reply yet)
...
GOING COLD: The Lees (8 days), Andres @ Supreme (6 days)
WAITING ON: Supreme Lending, Lee pre-approval (chase today)
```

## Who's waiting on Scotty (email)

Search Gmail for threads in the last 7 days where:
- the last message is **from someone else**, not Scotty, and
- it's addressed to Scotty directly (To:, not just CC), and
- it's not a newsletter, notification, or automated sender (no-reply, notifications@, marketing footers, "unsubscribe").

Useful query starting point: `in:inbox newer_than:7d -from:me -category:promotions -category:social -category:updates`. Then check each thread's last sender.

Rank by sender: a People row marked client or lead first, then any address on a thread with a known deal, then everyone else. Show the top 5 with how long they've waited. Offer to draft replies as Gmail drafts. Don't label, archive, or move anything; that belongs to the inbox skill.

Scotty has more than one address (scotty@hernandezhomegroup.com and scottyhernandez@epique.me). Treat both as "me."

## Who's waiting on Scotty (texts and calls)

Scotty's iMessages and texts sync to his iMac, so they can only be read by a Claude running **on the iMac** (Claude desktop app or Claude Code there). A cloud session can't reach the iMac.

**On the iMac:** read the Messages database read-only. It's at `~/Library/Messages/chat.db` and needs Full Disk Access granted to the app running Claude. Open it with `sqlite3 -readonly`, never write to it, and don't copy message contents anywhere except the ledger summary. Find conversations from the last 7 days where the latest message has `is_from_me = 0`. Match the handle (phone or email) to a People row, and use Contacts for the name if needed. Rank and present them the same way as email, in a separate **TEXTS** list.

Call history is in `~/Library/Application Support/CallHistoryDB/CallHistory.storedata` (also read-only). List missed calls from the last 2 days with no callback since.

**In the cloud (scheduled sweeps):** skip texts and calls. End the sweep with: "Texts aren't in this check. Say 'check my texts' from the iMac, or tell me any I should log."

## Midday sweep (around 12:30pm)

What's still open from Today, plus new inbound since the morning that's waiting on him. 5 lines max.

## End-of-day sweep (around 5:30pm)

1. Ask which Today items got done, or infer from sent mail, calendar, and Read AI meetings, then confirm.
2. Move done items to Done and update each person's `Last touch`.
3. Roll anything unfinished to tomorrow and say so plainly.
4. Pull action items from any Read AI meetings today that haven't been processed yet (Mode 3).
5. Close with: "Anything still in your head? Dump it and I'll file it."

## Scheduling

These run on demand. To make them automatic, set them up as scheduled routines (weekdays 7:45am, 12:30pm, and 5:30pm Central) that run this skill's sweep. Only create the schedule after Scotty confirms the times.
