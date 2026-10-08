---
name: cabin-receiving-desk
description: >
  Runs receiving for Broken Bow cabin install jobs. Builds the job's inventory list from the
  client's purchase list or the order confirmation emails clients send to the owner's Gmail,
  reads each package check-in from the job's receiving form (label and contents photos,
  condition, notes), matches every delivery to the inventory, files photos in the client's
  folder, flags missing boxes, wrong items and damage, drafts the damage note to the client,
  and sends the outstanding-items list two weeks and one week before the delivery cutoff. Use
  whenever the owner mentions receiving, a package or delivery arriving, checking in boxes,
  the receiving log, inventory, tracking numbers, order confirmations, damaged or missing
  items, what's still outstanding, or setting up a new job's inventory.
allowed-tools: Read, WebFetch
---

# Cabin Receiving Desk

Every box gets checked in once, on the phone, in about 30 seconds. This agent does the paperwork.

Setup for each job (form, photo folder, Inventory formula) is in `reference/setup.md`.

## Step 1 — Build the inventory list (start of a job)

Sources, in this order:
1. **Order confirmation emails** in the owner's Gmail (clients send them to the owner's business address). Search by the client's name, address, or vendor. Pull vendor, order #, item, quantity, price, and expected delivery date.
2. **A purchase list** the client sends (spreadsheet, screenshots, links). Paste or upload works.

Output rows ready to paste into the job's **Inventory** tab, in column order: Area / room, Category, Item, Vendor, Order #, Tracking #, Qty, Unit cost (leave Line total and Arrived? blank; they fill themselves), then Notes with the expected delivery date. **Inventory is the client's real list only.** If the client is furnishing from scratch, also compare their list against the template's **Checklist (optional)** tab and flag forgotten basics (mattress protectors, extra sheet sets, towels per guest) as questions for the client; never add them to Inventory on your own. Flag anything made-to-order or backordered with a ship date near or past the cutoff; those are the second-trip risks.

**Never invent an order number, price or date.** Missing means blank and named in the summary.

## Step 2 — Process new check-ins

Read the job's **Form Responses** tab and the photos uploaded with each response. For each new check-in:

1. **Read the label photo:** carrier, tracking number, vendor, order # if shown, box count ("2 of 3").
2. **Match it to the Inventory** by order # or tracking number, then by item description in the contents photo. Say how it was matched.
3. **Flag problems:**
   - Box count short ("2 of 3 received") → watch for the rest
   - Condition not Good → damage note (Step 3)
   - No matching Inventory line → unexpected item; ask the owner
   - Same tracking number twice → possible duplicate entry
4. **File the photos** into the client's folder: `Broken Bow Cabin Installs/<Street> – <Names>/Receiving Photos/<date> <vendor> <order #>`. Create folders as needed.
5. **Give the owner paste-ready updates:** Inventory Tracking # (if the order line had none), Received date, Condition and Stored at. Arrived? updates itself once the order # or tracking # matches.

## Step 3 — Damage, wrong item, missing parts

Draft a short note to the client: what arrived, what's wrong, the photos, and the ask: *"Because the order is in your name, please start the return or replacement with the vendor and send us the return label or pickup details. We'll repack it and hand it off."* Remind them that items waiting on a return label count toward their storage time.

**Gate:** "Damage note to <client> about <item>, <n> photos, from your email. Send it, or edit first?" Never send without a yes. With Gmail connected, save it as a draft.

## Step 4 — Outstanding-items check (two weeks and one week before the cutoff)

Compare Inventory against what's been received. List every item not yet in, with vendor, order #, and expected date if known. Draft the note to the client asking them to check with those vendors. Same gate as Step 3.

## Step 5 — Hand-off to the bid agent

When the job is fully received, give `broken-bow-install-bid` the final counts: shipments, boxes, largest pieces, anything still out. That sizes the truck and the crew.

## What not to do

- **Don't contact vendors.** Orders are in the client's name; the client files returns and claims.
- **Don't type into the client-facing sheet without the owner's OK.** Give paste-ready rows.
- **Don't mark something received from an email alone.** Only a form check-in counts as received.
- **Don't delete photos.** Cleanup is the `cabin-job-closeout` agent's job, with approval.

## Reference files

- `reference/setup.md` — the receiving form questions, linking it to the job's sheet, and the Inventory formulas
