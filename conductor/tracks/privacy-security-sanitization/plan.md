# Track Plan: Privacy & Security Sanitization

## Phase 1: Codebase Path Sanitization
- [ ] Refactor `tests/conftest.py` to use generic mock values for USER and HOME.
- [ ] Refactor `tests/test_isolate.py` to dynamically resolve `ISOLATE_PATH` and avoid hardcoded user paths in translation tests.

## Phase 2: Git & History Sanitization
- [ ] Remove existing personal logs from Git tracking (`session_log/*`, `skills/session_log/*`, etc.).
- [ ] Add `.gitkeep` files to maintain log directory structures.
- [ ] Delete orphaned `podman_debug.log` files from the repository.
- [ ] Update `.gitignore` to prevent future tracking of session logs.
- [ ] Create `.geminiignore` for efficient context management.
