# Gemini Workbench

This project serves as the centralized configuration and development hub for all Gemini CLI activities.

## Core Mandates
- **Native Sandboxing:** Use macOS Seatbelt (`sandbox-exec`) by default for lightweight, native protection.
- **Isolated Sandboxing:** Use `gemini-isolate` for full Ubuntu containerized isolation when necessary.
- **Unified Logging:** All sessions in this project are logged to the local `session_logs/` directory.
- **Centralized Binaries:** Custom wrappers (`gemini`, `gemini-shell`, `gemini-isolate`) are located in `bin/` and added to the host's `PATH`.

## Project Structure
- `bin/`: Host scripts and CLI wrappers.
- `config/`: Shared configuration settings for host and container.
- `skills/`: Custom agent skills (symbolically linked to `~/.gemini/skills`).
- `session_logs/`: Persistent history of all workbench activities.
