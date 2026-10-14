# The Melissa Buyers sheet

The buyer files live in one Google Sheet, **Melissa Buyers**, in the owner's Drive. It's the portable source of truth: if the owner changes CRMs or brokerages, File → Download → CSV takes every buyer along. Lofty (or the next CRM) holds contacts and conversations; this sheet holds what each buyer is looking for and what's been sent.

**The owner never has to fill it in.** Melissa writes it from consult notes and replies. The owner can edit any cell from their phone, and Melissa reads the sheet fresh on every run.

## Tab: Buyers (one row per buyer)

| Col | Header | Example |
|---|---|---|
| A | Buyer | Smiths |
| B | Status | Active / Paused / Under contract / Closed / Dead |
| C | Names | Jen & Mike Smith |
| D | Mobile 1 | +14055551234 |
| E | Mobile 2 | +14055555678 |
| F | Primary texter | Jen / Mike / Group |
| G | Email | |
| H | Market | OKC / Tulsa / Broken Bow |
| I | Areas | Edmond, Deer Creek SD, N OKC |
| J | Price min | 350000 |
| K | Price max | 425000 |
| L | Payment max | 2900 |
| M | Loan | VA |
| N | Beds min | 3 |
| O | Baths min | 2 |
| P | Sq ft min | 1800 |
| Q | Property type | Single family |
| R | Deal-breakers | busy road; HOA; flood zone |
| S | Must-haves | Deer Creek or Edmond schools; fenced yard; garage fits F-250; storm shelter or room to add |
| T | Nice-to-haves | shop; primary down; updated kitchen |
| U | Watch-outs | Mike works nights; Jen's mom may move in ~2 yrs |
| V | Commute | Mike → Tinker AFB ≤ 35 min at 6pm |
| W | Move by | 2027-03 |
| X | Matrix auto-email name | Homes in Bethany, Mustang, & Yukon |
| Y | Lofty alert / contact link | |
| Z | Notes | |

Separate list items with `;`.

## Tab: Sent

Date · Buyer · Address · Price · Link · MLS # · Owner note · Client response (owner fills or tells Melissa)

## Tab: Skipped

Date · Buyer · Address · Price · Link · MLS # · Reason

## Tab: Run log

Date/time · Source (MLS API / email / on demand) · Listings read · Out on deal-breaker (with reasons) · Shortlisted · Texted owner?

## Tab: Settings

| Setting | Value |
|---|---|
| Owner mobile | +1405… |
| Run times | 08:00, 12:00, 17:00 |
| Last run | (Melissa updates) |
| Alert senders | OKC@southcentralmatrixmail.com (Matrix Concierge), no-reply@lofty.com (Lofty) |
| Last digest | (Melissa updates; one waiting-on-you digest per day) |
| Owner signature for client texts | — Scotty |

## Moving to a new CRM

Download each tab as CSV. Buyers tab columns C–G import as contacts into nearly any CRM; R–V paste into a notes field.
