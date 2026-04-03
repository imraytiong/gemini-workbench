# Track Specification: Podman Auto-Recovery

## Vision
Eliminate manual sandbox maintenance by providing an automated, non-blocking recovery system for Podman.

## Core Components
- **`bin/sandbox-reset`**: The unified recovery script.
  - **Soft Reset**: `podman machine stop` (10s timeout).
  - **Hard Reset**: `kill -9` of orphaned VM processes + `podman machine stop`.
  - **Restore**: Ensures `podman machine start` is successful.
- **`bin/gemini-isolate` Integration**:
  - Automatically triggers recovery when a timeout is detected.
  - Interactive prompt: "Podman is unresponsive. Attempt recovery? [Y/n]".
- **Slash Command**: `/sandbox:reset` for manual intervention.

## Constraints
- **Guaranteed No-Hang**: Every operation must have a strict timeout using `run_with_timeout`.
- **macOS Specifics**: Handle specific VM backends like `qemu` and `vfkit`.
