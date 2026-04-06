# Gemini Workbench

This project serves as the centralized configuration and development hub for all Gemini CLI activities.

## 🌟 Ground Truth & Core Directives

These directives are absolute and override all general guidelines. They govern how the Gemini CLI operates within this project:

1. **Always Use the Roadmap:** Before starting or proposing work, you MUST check the `ROADMAP.md` and active `milestones/`. Ensure any suggested or active tasks align with the current strategic phase.
2. **Always Use Conductor:** When executing tasks, you MUST use the Conductor framework. Always consult the `conductor/` directory for active tracks, read their `spec.md` and `plan.md`, and strictly follow the documented workflow for that track.
3. **Always Remember Before Shutdown:** Before completing a final task or concluding a session, you MUST invoke the `remember` skill to log our session state and synchronize the history. This ensures a clean context handoff for the next session.

## Core Architecture
- **Full Isolation:** Use Podman for full Ubuntu containerized isolation by default for all workbench sessions.
- **Native Fallback:** The `gemini-isolate` wrapper handles container lifecycle, with native Node.js execution only when already inside the sandbox.
- **Session Continuity:** Session logging and history are handled by the `remember` extension.

## Installation & Setup
For new machines (like macOS with Podman), clone the repository and run:
```bash
bash setup-workbench.sh
```
This script automates:
- Prerequisite verification (`node`, `npm`, `podman`, `git`, `gemini`).
- Symlinking configurations to `~/.gemini`.
- Registering the workbench and projects with the Gemini CLI.
- Building the isolated Podman sandbox image.

## Project Structure
- `bin/`: Host scripts and CLI wrappers dynamically detecting host and workspace paths.
- `config/`: Shared configuration settings for host and container.
- `conductor/`: Project management, guidelines, and execution tracks.
- `milestones/`: High-level strategic goals.
- `policies/`: Workspace-specific portable safety policies.
- `skills/`: Custom agent skills (symbolically linked to `~/.gemini/skills/`).

## Workflows
- **Initialization:** If the user asks to "setup", "install", or "initialize" the workbench, you must immediately execute `bash setup-workbench.sh` and guide them through the final PATH configuration steps.
- **Agent Development:** For standards regarding Python tool building, LLM context, and Podman security, refer to `BEST_PRACTICES_AGENTIC.md`.
