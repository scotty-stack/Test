# Receiving Setup — once per job

About 10 minutes the first time, 2 minutes per job after that (copy the form).

---

## 1. The check-in form (Google Forms)

Create it once as "Package Check-in – TEMPLATE". For each job: **Make a copy**, rename it "Package Check-in – <Street>".

Settings: **Collect email addresses: Verified** (records who received it, and Crystal can be added later). Requires a Google sign-in, which file uploads need anyway.

Questions, in this order (the formulas below depend on it):

| # | Question | Type | Required |
|---|---|---|---|
| 1 | Vendor | Dropdown: Amazon, Wayfair, Target, Walmart, Home Depot, Lowe's, IKEA, Other | Yes |
| 2 | Order # | Short answer | No |
| 3 | Tracking # | Short answer | No |
| 4 | Boxes in this delivery | Number (short answer, number validation) | Yes |
| 5 | Condition | Multiple choice: Good / Damaged / Missing parts / Wrong item | Yes |
| 6 | Photos (label first, then contents, then any damage) | File upload: images, up to 10 files | Yes |
| 7 | Stored at | Dropdown: Garage left wall / Garage small bay / Other | No |
| 8 | Notes | Paragraph | No |

Tip: the agent reads tracking and order numbers off the label photo, so on a busy day you can skip questions 2 and 3.

**Phone:** open the form link in Chrome or Safari → Share → **Add to Home Screen**.

## 2. Link the form to the job's sheet

In the form: **Responses → Link to Sheets → Select existing spreadsheet →** the job's "<Street> Installation Guide". This adds a **Form Responses 1** tab. Columns: A Timestamp, B Email, C Vendor, D Order #, E Tracking #, F Boxes, G Condition, H Photos, I Stored at, J Notes.

Photos go to a Drive folder the form creates ("Package Check-in – <Street> (File responses)"). Move that folder into the client's folder; the agent files photos from there.

## 3. Inventory formula ("Arrived?")

In the job's **Inventory** tab, add a column header in **P1**: `Arrived?`. In **P2**, paste and fill down:

```
=IF($I2="","",IF(COUNTIF('Form Responses 1'!$D:$D,$I2)+COUNTIF('Form Responses 1'!$E:$E,$I2)>0,"Arrived","Waiting"))
```

It shows "Arrived" once a check-in has the same order # or tracking # as column I (Vendor / order #). Put the order # in column I when you build the inventory.

## 4. Setup tab: real "Received %"

Replace the Received % formula for each area with a count of "Arrived", for example for the whole job:

```
=IFERROR(COUNTIF(Inventory!P:P,"Arrived")/COUNTIF(Inventory!P:P,"?*"),0)
```
