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

Skip question 3. The agent decodes the tracking number from the label's barcode, so the only job is a good label photo: close, flat, in focus, the striped barcode fully in frame, no glare. Pull the yellow driver sticker aside if it covers the stripes. One label photo per box.

**Phone:** open the form link in Chrome or Safari → Share → **Add to Home Screen**.

## 2. Link the form to the job's sheet

In the form: **Responses → Link to Sheets → Select existing spreadsheet →** the job's "<Street> Installation Guide". This adds a **Form Responses 1** tab. Columns: A Timestamp, B Email, C Vendor, D Order #, E Tracking #, F Boxes, G Condition, H Photos, I Stored at, J Notes.

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
Inventory **J2** (Arrived? = a form check-in or a Receiving Log row with the same order # or tracking #):
```
=ARRAYFORMULA(IF((E2:E="")*(F2:F=""),"",IF((E2:E<>"")*(IFERROR(COUNTIF(INDIRECT("'Form Responses 1'!D:D"),E2:E),0)+COUNTIF('Receiving Log'!C:C,E2:E))+(F2:F<>"")*(IFERROR(COUNTIF(INDIRECT("'Form Responses 1'!E:E"),F2:F),0)+COUNTIF('Receiving Log'!D:D,F2:F))>0,"Arrived","Waiting")))
```
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
