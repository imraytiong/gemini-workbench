# Gemini Workbench

This project serves as the centralized configuration and development hub for all Gemini CLI activities.

## Core Mandates
- **Full Isolation:** Use Podman for full Ubuntu containerized isolation by default for all workbench sessions.
- **Native Fallback:** The `gemini-isolate` wrapper handles container lifecycle, with native Node.js execution only when already inside the sandbox.
- **Unified Logging:** All sessions in this project are logged to the local `session_logs/` directory.
- **Centralized Binaries:** Custom wrappers (`gemini`, `gemini-shell`, `gemini-isolate`, `build-sandbox`) are located in `bin/` and added to the host's `PATH`.

## Project Structure
- `bin/`: Host scripts and CLI wrappers.
- `config/`: Shared configuration settings for host and container.
- `skills/`: Custom agent skills (symbolically linked to `~/.gemini/skills`).
- `session_logs/`: Persistent history of all workbench activities.
