# Melissa on the Mac mini: one-time setup

About 45 minutes, most of it waiting on MLS saved searches.

---

## 1. Decide whose Apple ID the Mac mini uses for Messages

This decides who the texts come from. Pick one:

| | **A. The owner's Apple ID** | **B. Melissa's own Apple ID** |
|---|---|---|
| Client texts come from | The owner's real number ✅ | Melissa's email/number (clients see a stranger) |
| Android (green bubble) clients | ✅ with Text Message Forwarding on the iPhone | ❌ iMessage only |
| Melissa → owner shortlist | Lands in the owner's "note to self" thread (may not buzz the phone) | Arrives like a text from a person named Melissa ✅ |
| `read_replies.py` flag | `--self` | (none) |

**Recommended: A**, because clients should hear from the owner's number. Test the self-thread notification first (step 3). If the shortlists don't buzz the phone, keep A for client texts and have Melissa send the shortlist by email or push notification instead.

## 2. Messages + permissions

1. Messages → Settings → iMessage: sign in with the Apple ID from step 1.
2. For option A: iPhone → Settings → Messages → **Text Message Forwarding** → turn on the Mac mini (lets the Mac send green-bubble texts to Android clients).
3. System Settings → Privacy & Security:
   - **Full Disk Access** → add Terminal (so `read_replies.py` can read `~/Library/Messages/chat.db`)
   - **Automation** → allow Terminal to control Messages (macOS asks the first time you send)
4. Test from Terminal in the repo folder:
   ```
   skills/melissa/scripts/send_imessage.sh +1405XXXXXXX "Melissa · test, reply OK"
   ```
   Reply "OK" from the iPhone, then:
   ```
   python3 -I skills/melissa/scripts/read_replies.py --from +1405XXXXXXX --self   # drop --self for option B
   ```
   It should print your "OK".

## 3. Claude Code on the Mac mini

1. Install Claude Code and sign in with the same claude.ai account.
2. Clone this repo to the Mac mini (e.g. `~/Code/Test`) so Claude Code finds the `melissa` skill.
3. Connect **Gmail** and **Google Drive / Sheets** so Melissa can read MLS emails and the buyer sheet.
4. Create `~/Melissa/config.sh`:
   ```
   OWNER_HANDLE="+1405XXXXXXX"
   SELF_MODE=1      # 1 for option A, 0 for option B
   ```

## 4. The Melissa Buyers sheet

Ask Melissa: "Set up my buyer sheet." She creates **Melissa Buyers** in Drive with the tabs in `buyer-sheet.md`. Then fill in the Settings tab (owner mobile, run times, signature).

Moving buyers in from Lofty: export contacts as CSV, give it to Melissa, and she'll build rows and list the questions still missing for each buyer.

## 5. MLS saved searches (the listing feed)

You'll need two feeds because the metros use different MLSs:

- **OKC metro + Broken Bow / Hochatown → MLSOK**
- **Tulsa metro → the Tulsa-area MLS** (MLS Technology / Greater Tulsa REALTORS®), if you're a member. If not, Melissa covers Tulsa only on demand from listings you send her.

For each buyer, in each MLS that covers their area:
1. Create a saved search using the widened criteria Melissa gives you.
2. Name it **"Melissa – <Buyer last name>"**.
3. Set auto-email/notification to **your own email**, not the client's, and set it to send immediately or hourly. Melissa reads these; clients get only what you approve.
4. Forward the first notification email to Melissa so she learns the sender address and format.

## 6. MLS API (later; better data, no email parsing)

Ask MLSOK (and the Tulsa MLS) about **RESO Web API / IDX data access** for your brokerage. It usually needs the broker's signature and a vendor/data license agreement. Once you have the API key, store it in the macOS Keychain, never in this repo, and tell Melissa. She'll switch Step 2 to the API.

## 7. Running on a schedule (not set up yet: owner decision)

Melissa can check for listings at 8am / 12pm / 5pm, and watch for your SEND replies every 2 minutes, using macOS `launchd` to start Claude Code headlessly (`scripts/watch_replies.sh` is the reply watcher). Running unattended means deciding exactly which tools she may use with nobody watching. Keep it to: read Gmail, read/write the Melissa Buyers sheet, and the scripts in `skills/melissa/scripts/`. Nothing else.

Until that's set up, run her by hand: "Melissa, check for new listings" / "Melissa, I replied."

## Troubleshooting

- **`read_replies.py` says "unable to open database"** → Full Disk Access isn't granted to the app running it.
- **Text "sent" but never arrives on an Android phone** → Text Message Forwarding is off, or resend with `sms` as the third argument.
- **Melissa reads the same reply twice** → delete `~/Melissa/state.json`; the next run starts fresh from "now."
