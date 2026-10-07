---
name: broken-bow-install-bid
description: >
  Builds a bid for a Broken Bow cabin install job: receiving the client's furniture
  and decor shipments at the warehouse, hauling everything to the cabin in one trip,
  installing the design, hauling off the boxes and packaging, and optionally removing
  the cabin's existing furniture. Works out the job's cost line by line from the
  owner's rate card, shows the math, flags anything that could turn one trip into
  two, and drafts a client-facing bid the owner reviews before it goes out. Use
  whenever the owner mentions bidding, quoting, or pricing a Broken Bow job, a cabin
  install, a cabin refresh, a designer's furniture order, a client's shipments, a
  haul-off, getting rid of old cabin furniture, or says a new Broken Bow client
  reached out. Also use for Hochatown or Beavers Bend cabin work.
allowed-tools: Read, WebFetch
---

# Broken Bow Install Bid

Turn a client's design order and cabin details into a priced bid the owner can send.

The money in this job is lost in the parts nobody quotes: a late shipment that forces a second trip, a 40-minute gravel climb a box truck can't make, three days of storage that turned into three weeks, and a dumpster's worth of cardboard. This skill prices those on purpose.

## Step 0 — New lead with no purchase list yet? Send the overview

When a prospective client wants a proposal but has no final purchase list, don't bid numbers. Build the **preliminary overview** from `reference/preliminary-overview.md`: the six-step process, who does what, a bird's-eye timeline, how pricing works (rates, not totals), what's included, and what's needed for the exact bid. Come back to Step 1 once the list is final.

## Step 1 — Gather the job, from wherever it lives

The job lives in its **Installation Guide** sheet in Drive (one per client, copied from the HHG Installation Template and named "<Street> Installation Guide"). Search Drive for the client's street name or last name and read these tabs (layout in `reference/hhg-sheet-map.md`):

- **Setup** — bedrooms, bed layout, baths, guests, hot tub / fire pit / game room, the budget by area, and the "Questions for <client>" column
- **Inventory** — every item, qty, est. cost, ordered, received, installed
- **Receiving Log** — every delivery, boxes, condition, photos, where it's stored
- **Costs & Trades** — every trade, quote, who pays, billable, markup, status
- **Fee Research** — the market pricing models and the quote calculator

No sheet yet? Copy the HHG Installation Template for the new client, or take a pasted order list / design board and build the intake from that. Full checklist in `reference/job-intake.md`. The essentials:

- **The order list** — every item, vendor, quantity, box count if known, and ship status (ordered / shipped with tracking / delivered / backordered)
- **The cabin** — address, bedrooms, floors, stairs, driveway and road access
- **The install window** — the dates between guest stays when the cabin is empty
- **Scope** — install only, or install plus removal of existing furniture
- **What happens to the old furniture** — donate, sell, client keeps, or dump

**Name the gaps out loud.** Don't guess a box count or a driveway grade. List what's missing, ask in one message, or carry it into the bid as a stated assumption.

## Step 2 — Check the one-trip plan

The whole job is priced on one trip. Before pricing, test whether one trip is realistic:

- **Inventory vs. Receiving Log** — every Inventory line should have a delivery in the Receiving Log by the cutoff. If the Inventory's Ordered / Qty received columns are blank but the Receiving Log has deliveries, the two aren't being kept in sync — say so, because "Received %" on Setup will read 0% and can't be trusted.
- **Open questions** — anything still in the "Questions for <client>" column (final item list, which design to install from) is a blocker for a fixed price. Carry each one into the bid as an assumption.
- **Shipments** — any item not yet delivered to the warehouse, backordered, or with a ship date within 5 business days of the load date is a second-trip risk. Name each one.
- **Truck fit** — estimate load volume from the order list using `reference/load-sizing.md`. If it's over the truck's usable capacity in the rate card, say which truck/trailer combo fits or that it needs two.
- **Access** — steep or unpaved drives, tight turns, and low clearance can force a smaller truck plus a shuttle. Flag them.

Output: **One trip: yes / at risk / no**, with the specific reasons.

## Step 3 — Price it from the rate card

Read `reference/rate-card.md` (the owner's numbers) and `reference/pricing-lines.md` (how each line is calculated). Price every line and show the arithmetic so the owner can check it in ten seconds:

The formula: **15% of the final order total (the owner's fee, theirs alone) + the U-Haul at cost + helper labor**, plus pass-throughs and add-ons. Storage is shown at its full value, then marked complimentary.

1. Design fee: 15% x order total. Use the final order list if it exists, otherwise the Setup budget, labeled as an estimate that adjusts to the final order total
2. U-Haul: a real quote for the truck size the cabin needs (mileage, fuel, coverage, pads) billed at cost
3. Helper labor: helper rate x helpers x days (load, drive, install, drive home)
4. Lodging and travel, at cost
5. Trash and packaging haul-off and disposal
6. Optional: existing furniture removal, by disposition
7. Storage: its full value shown, then "included at no charge"; billed only past the free period
8. Second-trip line (conditional, priced separately, not buried)
9. Trades passed through (paint, electrical, carpentry, cleaning, decks): quoted cost + markup, and who pays the trade directly

Show what the owner keeps apart from the bid total: the design fee (owner only) and any markup on trades.

**Never invent a rate.** If the rate card has a blank, leave the line as `$______` with exactly what's needed, and price everything else. Read [absent-is-not-zero](../../shared/absent-is-not-zero.md) if present: a missing rate is not a free line.

If past bids or invoices are available, compare the total to the closest one and say if it's more than 15% off.

## Step 4 — Show the owner the bid sheet

Internal view first, before anything client-facing:

```
Smith cabin — 4BR, 2 floors, Hochatown
Install window: Tue Nov 10 – Thu Nov 12 (between guest stays)
One trip: AT RISK — the dining table (Vendor X) is backordered to Nov 6

Line                      Math                          Amount
Design fee                15% x $__ design budget       $...
U-Haul                    <truck> quote for <date>      $...
Crew                      $200 x 2 helpers x 3 days     $...
...
Total                                                   $...
Margin check              cost $... / price $...        ...%

Assumptions going into the bid: ...
Missing: ...
```

Then the decision points, in one message:

- Price the backordered items as a second trip now, or exclude them?
- Anything here you'd move up or down?

## Step 5 — Draft the client bid

Draft from `reference/bid-template.md`, in the owner's voice (read [the voice profile](../../shared/voice-profile.md) if it exists). It must include:

- What's included and what's not, in plain words
- The install window and what it depends on (all items delivered by the cutoff date)
- The order total wording: the fee is 15% of the final order total, so it adjusts if items are added or removed
- Complimentary storage, with its value, so the client sees what they're getting
- The second-trip terms and the storage cutoff, so a late shipment isn't a surprise invoice
- Damage terms: items are inspected on arrival; vendor damage claims are the client's, with the owner's help
- Deposit and payment terms from the rate card

Also output the priced lines as rows ready to paste into the job's **Costs & Trades** tab (Type, Trade / vendor, Scope, Room, Quoted, Paid by, Billable, Markup %, Status = Quoted), and a separate list of "our cut" lines for the private Income sheet (who earns it: owner, partner, or both; the 15% design fee is always the owner's alone). **The Income sheet numbers never go into anything the client sees.**

Produce DOCX or PDF. With Gmail connected, save it as a **draft** to the client.

**Gate:** "Bid for <client>, <total>, <scope>, saved as a draft to <email> from your address. Send it, or edit first?" Never send without a yes. For e-signature and the deposit invoice, hand off to `proposal-builder`.

## Step 6 — After it's accepted

Offer, don't assume: put the install window and load date on the calendar, and set a shipment cutoff reminder 7 days before load date to chase any undelivered items.

## What not to do

- **Don't price one trip when the shipments say two.** That's the most common way this job loses money.
- **Don't bury contingency in other lines.** A visible second-trip line is easy to explain; a padded install line isn't.
- **Don't invent a rate, distance, or box count.** Blank and named beats plausible and wrong.
- **Don't send anything to the client without the owner's yes.**
- **Don't count pass-through money as income.** Trip fuel and lodging billed at cost, the U-Haul's and helpers' actual cost, and trades the client pays are not "our cut." Only the markup on top is.
- **Don't promise donation pickup or resale results.** Quote the haul; outcomes depend on the charity or buyer.

## Reference files

- `reference/hhg-sheet-map.md` — the Installation Guide tabs and columns, and known traps in them
- `reference/rate-card.md` — the owner's rates. Fill this in once; every bid uses it.
- `reference/job-intake.md` — the full intake checklist, every angle
- `reference/load-sizing.md` — estimating truck volume from an order list
- `reference/pricing-lines.md` — how each line is calculated
- `reference/bid-template.md` — the client-facing bid layout and standard terms
- `reference/preliminary-overview.md` — the pre-bid overview for new leads
