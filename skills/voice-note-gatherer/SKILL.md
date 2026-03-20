---
name: voice-note-gatherer
description: Automates the extraction of voice notes (specifically from PLAUD.AI) sent to the Gmail alias 'raymond.tiong+plaud@gmail.com'. It converts these emails into Markdown files and saves them in the project's 'journal/voice_notes/' directory.
---

# Voice Note Gatherer

This skill helps you keep your PLAUD voice notes organized within your project by automatically fetching them from your Gmail and converting them into Markdown.

## Prerequisites

1.  **Gmail App Password:** You MUST generate an App Password for your Gmail account at [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords).
2.  **Environment Variables:** You must set the following environment variables in your terminal or shell profile:
    *   `GMAIL_USER`: Your full Gmail address (e.g., `raymond.tiong@gmail.com`).
    *   `GMAIL_PASS`: Your 16-character Gmail App Password.

## Workflow

When the user asks to "gather voice notes," "sync PLAUD notes," or "check for new notes," follow these steps:

1.  **Execute Gatherer:** Run the `scripts/gather_notes.cjs` script.
    - **Command:** `node <path-to-skill>/scripts/gather_notes.cjs`
2.  **Process:** The script will connect to your Gmail, search for emails sent to `raymond.tiong+plaud@gmail.com`, and save new notes to `rayintheloop_web/journal/voice_notes/`.
3.  **Confirm:** Tell the user how many new notes were gathered and provide the filename(s) of the most recent ones.

## File Locations

- **Target Directory:** `rayintheloop_web/journal/voice_notes/`
- **Duplicate Tracking:** `processed_ids.json` (within the skill directory)
- **Skill Path:** `skills/voice-note-gatherer/`
