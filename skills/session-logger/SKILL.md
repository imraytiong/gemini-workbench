---
name: session-logger
description: Automates session logging to the project workspace and Git. Use this to summarize the current state and maintain a detailed, reverse-chronological history in 'session-history.md'. The 'latest-session.md' file is automatically updated with a consolidated 'Day View' aggregating all activities from the current date for rapid context recovery.
---

# Session Logger

This skill provides a structured way to maintain a persistent record of your work in the project workspace and Git history.

## Workflow

When the user asks to "log this session," "save our work," or "checkpoint," follow these steps:

1.  **Synthesize:** Create a clear, technical summary of what was accomplished in the current session and a list of specific, actionable pending tasks.
2.  **Execute Logger:** Use the `scripts/log_session.cjs` script to update the project workspace.
    - **Command:** `node <path-to-skill>/scripts/log_session.cjs "<Title>" "<Summary>" "<Tasks>" ["<Plan>"] ["<Outcome>"] ["<NextSteps>"]`
    - **Title:** A concise name for the current work block (e.g., "Meta-workflow Setup").
    - **Summary:** A bulleted list or paragraph of technical accomplishments.
    - **Tasks:** A bulleted list of items for the next session.
    - **Plan (Optional):** The proposed strategy for the session.
    - **Outcome (Optional):** The execution and validation details.
    - **NextSteps (Optional):** Actionable items to be highlighted in the daily summary.
3.  **Confirm:** Tell the user the workspace has been updated and the changes committed to Git.

## Context Recovery

When starting a new session or if the user asks "where did we leave off?", you SHOULD:

1.  Read the `session_logs/latest-session.md` file in the project root to instantly recover the full context of the current day's activity.
2.  Acknowledge the daily progress and offer to start on the consolidated pending tasks.

## File Locations

- **Long-running Log:** `session_logs/session-history.md` (Reverse-chronological history)
- **Daily Capture:** `session_logs/latest-session.md` (Aggregated 'Day View' - Overwritten each time)
- **Skill Path:** `skills/session-logger/`
