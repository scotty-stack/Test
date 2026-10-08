# Installation Guide — Sheet Map

New jobs use **Cabin Install Template (clean)**: tabs Job Summary, Inventory, Receiving Log, Costs & Trades, Bid, Checklist (optional). Column map and formulas: `skills/cabin-receiving-desk/reference/setup.md`. The table below describes the **older** layout, still used by sheets made before October 2026.

One Google Sheet per client, copied from **Cabin Install Template**. A separate **<Street> Income (Private)** sheet holds the money split and is never shared with the client.

---

## Tabs

| Tab | What it holds | Bid uses it for |
|---|---|---|
| Setup | Address, client, bedrooms, beds, baths, guests, hot tub / fire pit / game room, linen and towel par, budget by area with Received %, "Questions for <client>" column | Cabin size, furnishing budget, open questions |
| Inventory | Area, Category, Item, Qty rule, Qty, Est. unit cost, Est. total, Ordered, Vendor / order #, Qty received, Received date, Condition, Installed, Location in house, Notes | Order list, load size, install hours |
| Receiving Log | Date, Vendor, Order #, Carrier / tracking, Boxes, Items, Condition, Received by, Photos, Stored at, Notes / claim # | What's arrived, damage, storage days, box count |
| Costs & Trades | Date, Type, Trade / vendor, Scope, Room, Contact, Quoted, Actual cost, Paid by, Billable, Markup %, Amount to bill, Scheduled date, Status, Date paid, Invoice #, Notes | Where the bid's lines land |
| Fee Research | Market pricing models with sources, quote calculator off the furnishing budget | Market check on the 15% design fee |

Income (Private): Item, What client is billed, Our cut, Who earns it (owner / partner / both), share %, owner $, partner $, Status, Date received.

## Traps to check on every job

- **Inventory not synced to the Receiving Log.** Deliveries get logged, but the Inventory tab's Ordered / Qty received columns stay blank, so Setup shows 0% received.
- **Template example row left in** the live Receiving Log.
- **Date typos** (wrong year, missing year). These break the storage-day math.
- **Blank Received by / Stored at / Photos** on deliveries. Gaps weaken any damage claim.
- **"Our net" formula.** It reads billed minus "Paid out by us". When the client pays trades directly, it overstates what you keep. Real kept income is on the Income sheet.
- **Amount to bill doesn't match actual cost** on pass-through lines. Check for typos.
- **Previous client's name and address left in the template titles.** Clear them when copying for a new client.
- **Leftover test text** in item names.
