# Call capture

The goal: every client conversation leaves a written trace the assistant can read, so commitments made on the phone turn into follow-ups automatically.

## What's already covered

- **Zoom meetings** are recorded and summarized by **Read AI**, which is already connected. Mode 3 reads `action_items` and `summary` from Read AI. Nothing to set up.
- **Google Meet and Teams** are covered by Read AI too, if its calendar auto-join is on for those.

## Cell phone calls: Scotty's choice is iPhone recording

As of October 2026, Scotty records cell calls with the iPhone's built-in recorder. He may move to a business line in 2027. The workflow:

1. During a client call, tap the record button. iPhone announces it to the other person.
2. After the call, the recording, transcript, and summary land in the Notes app (Call Recordings folder), and Notes syncs to the iMac.
3. To get it to the assistant: share the transcript into chat, or save it to the Drive folder **"Call Transcripts."** When Claude is running on the iMac, it can also read today's call-recording notes straight from Notes.
4. No time to share it? A 20-second voice note works ("just talked to Maria, she wants to counter at 315, I owe her comps tomorrow").

## Other options (for later)

1. **iPhone's built-in call recording** (iOS 18.1 and later): tap the record button during a call. iPhone announces the recording to both sides automatically, and the recording plus a transcript and summary are saved to the Notes app. Free, nothing to install. To get it to the assistant, share the transcript into chat or save it to a Drive folder named **"Call Transcripts"** that the after-call mode reads.
2. **A business line app (OpenPhone/Quo, RingCentral, Dialpad)**: auto-records every call on the business number, transcribes it, and emails or Slacks a summary. This is the most hands-off option, because the assistant can find the summaries in Gmail on every sweep with no tapping. It also keeps client calls off the personal number.
3. **Read AI or Otter mobile app**: records in-person conversations such as showings and listing appointments. Phone-call support varies by app and platform.
4. **Google Voice**: records **incoming** calls only (press 4). Better than nothing, but it misses calls Scotty makes.

## Consent: do this right

- **Oklahoma, Texas, and Arkansas are one-party consent states**, so Scotty may legally record calls he's part of.
- **Some states require everyone's consent**, including California, Florida, Washington, Illinois, Pennsylvania, Maryland, Massachusetts, Montana, New Hampshire, Michigan (by some court readings), and Connecticut and Nevada for phone calls. When the person on the other end is in one of these states, the stricter rule applies. Out-of-state buyers relocating to Oklahoma are common, so this matters.
- **Simplest safe habit:** announce it on every call. For example: "Hey, I record my calls so I don't miss any details for you. That okay?" iPhone's automatic announcement already covers this.
- Check whether the brokerage (Epique) has a recording policy, and keep recordings only as long as needed.
- This is general information, not legal advice. For a firm answer, ask the brokerage or a lawyer.

## Getting transcripts to the assistant

Any of these work, from least to most automatic:
- Paste or share the transcript into chat: "just got off with Maria, here's the transcript."
- Drop transcript files into the Drive folder **"Call Transcripts"**. The end-of-day sweep reads anything added today.
- Business phone app summaries emailed to Gmail. The sweep searches for them by sender.

If none of these happened, a 20-second voice note after the call works almost as well: "Just talked to Maria, she wants to counter at 315, I owe her comps by tomorrow." That's a brain dump, and Mode 1 files it.
