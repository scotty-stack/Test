# Receiving Setup — once per job

About 10 minutes the first time, 2 minutes per job after that (copy the form).

---

## 1. The check-in form (Google Forms)

The master copy is **Package Check-In - Template** in `_Templates`. For each job: open it → ⋮ → **Make a copy**, rename it "Package Check-In - <Street>", and move it into the client's folder.

Settings: **Collect email addresses: Verified** (records who received it, and Crystal can be added later). Requires a Google sign-in, which file uploads need anyway.

Questions, in this order. Photos come first so you snap the pictures before typing anything:

| # | Question | Type | Required |
|---|---|---|---|
| 1 | Photos: 1) label 2) everything from the box laid out 3) any damage | File upload: images, up to 10 files | Yes |
| 2 | Vendor (who sold it, not the carrier) | Dropdown: Amazon, Wayfair, Minoan, Target, Walmart, Home Depot, Lowe's, IKEA, Other | Yes |
| 3 | Boxes in this delivery | Number (short answer, number validation) | Yes |
| 4 | Condition | Multiple choice: Good / Damaged / Missing parts / Wrong item | Yes |
| 5 | Stored at | Dropdown: Front living room / Garage left wall / Garage small bay / Other | Yes |
| 6 | Tracking # | Short answer | No |
| 7 | Order # (only if printed on a packing slip, not the TBA number) | Short answer | No |
| 8 | Notes (what's inside, e.g. "3 sheet sets") | Paragraph | No |

Photos that make matching work: a flat, in-focus label shot with the barcode fully in frame (lift the yellow driver sticker off the stripes), then everything from the box laid out together with product names facing the camera. Type the tracking number when you can; the agent decodes the label barcode as a backup and to catch typos.

Moving or renaming questions never changes the linked sheet's column order, so the formulas below keep working.

**Phone:** open the form link in Chrome or Safari → Share → **Add to Home Screen**.

## 2. Link the form to the job's sheet

In the form: **Responses → Link to Sheets → Select existing spreadsheet →** the job's "<Street> Installation Guide". This adds a **Form Responses 1** tab. The agent finds columns by their header names, not position, because a form copied from the template lists them in question order (Timestamp, Email, Photos, Vendor, Boxes, Condition, Stored at, Tracking #, Order #, Notes) while older forms differ. The Arrived? formula reads the Tracking # and Order # columns by header too (see below).

Photos go to a Drive folder the form creates ("Package Check-in – <Street> (File responses)"). Move that folder into the client's folder; the agent files photos from there.

## 3. The job's sheet (Cabin Install Template (clean))

Make a copy of **Cabin Install Template (clean)** from `_Templates` for each job, rename it "<Street> Installation Guide", and move it into the client's folder. Link the form to it (step 2).

### Inventory columns
A Area / room · B Category · C Item · D Vendor · **E Order #** · **F Tracking #** · G Qty · H Unit cost · I Line total (auto) · **J Arrived? (auto)** · K Received date · L Condition · M Stored at · N Placement in cabin · O Installed · P Notes

Inventory holds **the client's real purchase list only.** Never the checklist.

### The auto formulas (already in the template; paste back only if one is ever cleared)
Inventory **I2**:
```
=ARRAYFORMULA(IF((G2:G="")+(H2:H=""),"",G2:G*H2:H))
```
Inventory **J2** (Arrived? = the item's order # or tracking # matches any answer in the form's "Tracking…" or "Order…" column, or the Receiving Log. It finds those form columns by their header names, so it works however the form's questions are ordered, and it ignores spaces and capitals):
```
=ARRAYFORMULA(IF((E2:E="")*(F2:F=""),"",IF(((E2:E<>"")*ISNUMBER(SEARCH("|"&UPPER(SUBSTITUTE(E2:E," ",""))&"|","|"&UPPER(SUBSTITUTE(TEXTJOIN("|",TRUE,IFERROR(INDEX(INDIRECT("'Form Responses 1'!A2:Z"),0,MATCH("Tracking*",INDIRECT("'Form Responses 1'!A1:Z1"),0)),""),IFERROR(INDEX(INDIRECT("'Form Responses 1'!A2:Z"),0,MATCH("Order*",INDIRECT("'Form Responses 1'!A1:Z1"),0)),""),'Receiving Log'!C3:D)," ",""))&"|"))+(F2:F<>"")*ISNUMBER(SEARCH("|"&UPPER(SUBSTITUTE(F2:F," ",""))&"|","|"&UPPER(SUBSTITUTE(TEXTJOIN("|",TRUE,IFERROR(INDEX(INDIRECT("'Form Responses 1'!A2:Z"),0,MATCH("Tracking*",INDIRECT("'Form Responses 1'!A1:Z1"),0)),""),IFERROR(INDEX(INDIRECT("'Form Responses 1'!A2:Z"),0,MATCH("Order*",INDIRECT("'Form Responses 1'!A1:Z1"),0)),""),'Receiving Log'!C3:D)," ",""))&"|")))>0,"Arrived","Waiting")))
```
One tracking or order number per Inventory row. Pasting values over columns I or J deletes these formulas; paste A–H and K–P separately.
Costs & Trades **L9**:
```
=ARRAYFORMULA(IF(J9:J="Y",IF(H9:H<>"",H9:H,G9:G)*(1+IF(K9:K="",0,K9:K)),""))
```

### Other tabs
- **Job Summary:** client info, job type, open questions; dates (enter load day → cutoff, last item received, free-storage end, days to cutoff); receiving status; money (order total, fee, bid).
- **Receiving Log:** backup for anything checked in without the form. Header is row 2.
- **Bid:** the pricing calculator (15% / $3,500 minimum, U-Haul, helpers × days × $225, extra trips, included value, payment schedule).
- **Checklist (optional):** "did we forget anything?" rules for clients furnishing from scratch.

Older job sheets (built from the old template) use the old layout: a single "Vendor / order #" column (I) and "Arrived?" in P. Match on whichever layout the sheet has.
