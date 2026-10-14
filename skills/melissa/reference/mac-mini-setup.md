# Melissa on the Mac mini: one-time setup

About 30 minutes. Do it sitting at the Mac mini.

---

## 1. Messages uses the owner's Apple ID

Decided: the Mac mini's Messages is signed in to the **owner's** Apple ID, so client texts come from the owner's real number. Melissa and the owner talk in the owner's **note-to-self** thread (texts to your own number). Every message Melissa writes there starts with `Melissa ·`, and anything else in that thread is read as the owner talking to her.

1. Messages → Settings → iMessage: signed in with your Apple ID, and your phone number checked under "You can be reached at".
2. iPhone → Settings → Apps → Messages → **Text Message Forwarding** → turn on the Mac mini (lets it text Android clients).
3. System Settings → Privacy & Security:
   - **Full Disk Access** → add **Terminal** and `/bin/bash` (the scheduled jobs run through bash; press ⌘⇧G in the file picker and type `/bin/bash`)
   - **Automation** → allow Terminal to control Messages (macOS asks the first time)
4. System Settings → Energy: **Prevent automatic sleeping** on. Leave the Mac logged in. The jobs and Messages need a logged-in session.

## 2. Claude Code on the Mac mini

1. Install Claude Code and sign in with the same claude.ai account.
2. Clone this repo, e.g. `~/Code/Test`, and `cd` into it.
3. Make sure the **Gmail**, **Google Sheets** and **Google Drive** connectors show up: run `claude mcp list`. Note the exact names. If they don't start with `claude_ai_Gmail`, `claude_ai_Google_Sheets` and `claude_ai_Google_Drive`, fix the three `*_MCP` lines in `~/Melissa/config.sh` after step 3.

## 3. Install Melissa's schedule

From the repo folder:

```
skills/melissa/scripts/install.sh +14054201941
```

This writes `~/Melissa/config.sh` (your number, run times, connector names) and starts two background jobs:

| Job | When | What |
|---|---|---|
| `com.melissa.search` | 8:05am, 12:05pm, 5:05pm | Steps 2–4: new listings → shortlists; the waiting-on-you digest |
| `com.melissa.replies` | every 2 min | Checks for a text from you. Only if there is one does Melissa wake up (Steps 5–6), so it costs nothing while you're quiet |

Change times: edit `SEARCH_HOURS` in `~/Melissa/config.sh`, run `install.sh` again. Stop everything: `skills/melissa/scripts/uninstall.sh`.

**What Melissa can do unattended** (set in `scripts/melissa_claude.sh`): read Gmail; read and write her buyer sheet; find it in Drive; run her own scripts; and, once set, reach the MLS API host. That's all. She can't send email, delete or share files, or run other commands. Client texts go only through `send_to_client.py`, which checks your SEND reply in Messages before anything goes out.

## 4. Test the loop (5 minutes)

```
skills/melissa/scripts/text_owner.sh "test, reply OK"
```

1. **Did your iPhone buzz?** Texts to yourself sometimes arrive silently. If it didn't buzz, open the note-to-self thread on the iPhone → tap the name at the top → make sure **Hide Alerts** is off. Still silent? Tell Melissa. The fallback is to send her shortlists as email or push notifications and keep Messages for client texts.
2. Reply `OK` from the iPhone, wait 2 minutes, and check `~/Melissa/melissa.log`: Melissa should have woken up and answered you.

## 5. The Melissa Buyers sheet

Ask Melissa: "Set up my buyer sheet." She creates **Melissa Buyers** in Drive with the tabs in `buyer-sheet.md`, then walks the clients she found in your Matrix auto-emails and Lofty alerts (Alma E, Delaney Jones, Eli Riddle, Jay Jones, John & Lauren Reeves, Clint Harris, Melissa, Nalani Anderson, Reese Miner…) and asks which are active and what's missing for each.

## 6. The MLS API (the listing data)

The alert emails only say "new matches, log in to see." To screen listings on her own, Melissa needs the MLS's data feed.

MLSOK's Matrix is run by **Cotality** (it says so at the bottom of every Concierge email), and Cotality distributes MLS data through its **Trestle** platform. Ask MLSOK support:

> "I'd like a RESO Web API feed of active listings for my own use as an agent: a personal buyer-matching tool, not a public website. Is that through Trestle? Which license type and agreements do I need, and does my broker need to sign?"

Expect a data license agreement, your broker's signature, and possibly a monthly fee. Ask for **IDX** at minimum; "VOW" or "broker back-office" access includes more fields. When approved:

1. Put the API credentials in the macOS Keychain, **never in this repo or in config.sh**:
   ```
   security add-generic-password -s melissa-mls -a "<client id>" -w "<client secret>"
   ```
2. Set `MLS_API_HOST` in `~/Melissa/config.sh` to the API's host name.
3. Tell Melissa. She'll add the small script that pulls listings, and that host becomes the only website she can reach on scheduled runs.

**Tulsa:** the Tulsa metro is a different MLS (MLS Technology / Greater Tulsa REALTORS®). If you're a member there, ask them the same question; if not, Melissa covers Tulsa from listings you send her.

## Troubleshooting

- **Log says "unable to open database"** → Full Disk Access is missing for Terminal or `/bin/bash`.
- **Log shows a tool was denied** → the connector names in `config.sh` don't match `claude mcp list`.
- **Text "sent" but never arrives on an Android phone** → Text Message Forwarding is off.
- **Melissa answers an old text** → delete `~/Melissa/state.json`; she starts fresh from "now".
- **Nothing runs at all** → `launchctl list | grep melissa`; re-run `install.sh`; check `~/Melissa/launchd.log`.
