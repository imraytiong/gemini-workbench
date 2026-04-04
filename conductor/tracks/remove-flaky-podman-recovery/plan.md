# Track Plan: Remove Flaky Podman Recovery

## Phase 1: Removal of reset scripts and commands
- [x] Delete `bin/sandbox-reset`.
- [x] Delete `commands/sandbox/reset.toml`.
- [x] Remove `/sandbox:reset` entry from `commands/roadmap.toml` (if it exists).

## Phase 2: Refactoring of core wrappers
- [x] Strip out auto-recovery logic from `bin/gemini-isolate`.
- [x] Ensure `bin/gemini-isolate` still correctly detects timeouts/errors but doesn't attempt a reset.

## Phase 3: Validation
- [x] Verify that no references to the deleted files remain in the codebase.
- [x] Run existing tests (`pytest tests/test_isolate.py`) to ensure no regressions were introduced.
