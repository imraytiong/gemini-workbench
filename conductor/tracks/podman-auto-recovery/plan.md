# Track Plan: Podman Auto-Recovery

## Phase 1: The Reset Script (`bin/sandbox-reset`)
- [x] Implement `run_with_timeout` helper within the script.
- [x] Implement soft reset logic (timeout: 10s).
- [x] Implement hard reset logic (force kill orphaned processes).
- [x] Add Podman machine restart logic.
- [x] Test reset on a wedged machine.

## Phase 2: CLI Command Integration
- [x] Create `.gemini/commands/sandbox/reset.toml`.
- [x] Map command to `/sandbox:reset`.
- [x] Link to global `~/.gemini/commands/` via `setup-workbench.sh`.

## Phase 3: Auto-Recovery Logic in Wrapper
- [x] Update `bin/gemini-isolate` to detect timeouts.
- [x] Implement interactive recovery prompt.
- [x] Integrate `bin/sandbox-reset` into the automated failure block.
