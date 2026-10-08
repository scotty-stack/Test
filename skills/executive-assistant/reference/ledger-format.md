# EA Ledger format

Google Doc in Drive, exact name **"EA Ledger: Scotty Hernandez"**. Plain text with simple markdown-style headings so it reads cleanly in Docs and parses reliably. Every update writes a fresh full copy and trashes the previous one (see "How to save" in SKILL.md), keeping section order.

## Defaults

- Time zone: America/Chicago.
- Follow-up with no date: **next business day** for clients and leads, **3 business days** for vendors, lenders, title, and partners.
- Waiting-on with no chase date: **2 business days**.
- Going cold: an active client with no touch in **7 days**, or a lead in **3 days**. Past clients are handled by the monthly past-client check-in skill, not here.
- Done items older than 14 days are deleted from the ledger. The calendar and Gmail keep the history.

## Template

```
# EA Ledger: Scotty Hernandez
Last updated: <YYYY-MM-DD h:mm am/pm>

## Today
1. <must-do>  [from: Follow-ups / Reminder / Task]
(5 max. Rebuilt every morning sweep.)

## Reminders
- <YYYY-MM-DD h:mm> | <what> | cal: <event id>

## Follow-ups (I owe)
- [ ] <Person> | <what I owe them> | due <YYYY-MM-DD> | via <call/text/email> | added <date>

## Waiting on (they owe me)
- [ ] <Person/company> | <what> | chase <YYYY-MM-DD> | added <date>

## Tasks
- [ ] <task> | due <date or "—"> | added <date>

## People
### <Full name>  (<type: buyer / seller / lead / past client / lender / title / vendor / partner>)
- Contact: <phone> · <email>
- Property / deal: <address or "searching: 3bd OKC under $350k">
- Stage: <lead / active / under contract (close <date>) / closed / nurture>
- Last touch: <YYYY-MM-DD> <call/text/email/meeting> | <one line>
- Next touch: <YYYY-MM-DD> | <why>
- Notes: <family, preferences, things to remember>

## Ideas / someday
- <idea> | added <date>

## Inbox (unsorted)
- <raw line exactly as said> | added <date>

## Done (last 14 days)
- <YYYY-MM-DD> <item>
```

## Rules

- One person, one row. Merge duplicates when you notice them and mention the merge.
- Keep the raw wording of anything filed under Inbox (unsorted) so nothing gets lost in a paraphrase.
- Never store full SSNs, bank account numbers, or loan numbers in the ledger. Write "on file with lender" instead.
