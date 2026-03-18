# Gemini Workbench

This project serves as the centralized configuration and development hub for all Gemini CLI activities.

## Core Mandates
- **Standardized Environment:** Use the `Dockerfile.sandbox` for all Ubuntu-based containerized operations.
- **Unified Logging:** All sessions in this project are logged to the local `session_logs/` directory.
- **Centralized Binaries:** Custom wrappers and tools are located in `bin/` and should be added to the host's `PATH`.

## Project Structure
- `bin/`: Host scripts and CLI wrappers.
- `config/`: Shared configuration settings for host and container.
- `skills/`: Custom agent skills (symbolically linked to `~/.gemini/skills`).
- `session_logs/`: Persistent history of all workbench activities.
