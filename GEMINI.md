# Gemini Workbench

This project serves as the centralized configuration and development hub for all Gemini CLI activities.

## Core Mandates
- **Full Isolation:** Use Podman for full Ubuntu containerized isolation by default for all workbench sessions.
- **Native Fallback:** The `gemini-isolate` wrapper handles container lifecycle, with native Node.js execution only when already inside the sandbox.
- **Unified Logging:** All sessions in this project are logged to the local `session_logs/` directory.
## Installation & Setup
For new machines (like macOS with Podman), clone the repository and run:
```bash
bash setup-workbench.sh
```
This script automates:
- Prerequisite verification (`node`, `npm`, `podman`, `git`, `gemini`).
- Symlinking skills to `~/.gemini/skills`.
- Registering the workbench and projects with the Gemini CLI.
- Building the isolated Podman sandbox image.

## Custom Binaries
Custom wrappers (`gemini`, `gemini-shell`, `gemini-isolate`, `build-sandbox`) are located in `bin/`. These are now portable and dynamically detect the host username and workspace paths.

## Workflows
- **Initialization:** If the user asks to "setup", "install", or "initialize" the workbench, you must immediately execute `bash setup-workbench.sh` and guide them through the final PATH configuration steps.

## Project Structure
- `bin/`: Host scripts and CLI wrappers.
- `config/`: Shared configuration settings for host and container.
- `skills/`: Custom agent skills (symbolically linked to `~/.gemini/skills`).
- `session_logs/`: Persistent history of all workbench activities.
