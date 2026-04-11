# Track Plan: Transition to Native Default Execution

## Phase 1: Update Wrapper Logic
- [x] Refactor `bin/gemini` to set `NOSANDBOX=true` by default.
- [x] Add parsing for a `--sandbox` or `-s` flag to set `NOSANDBOX=false`.
- [x] Ensure existing logic (session restoration prompts) works correctly in native mode.

## Phase 2: Decouple Setup Scripts
- [x] Modify `setup-workbench.sh` to make Podman optional. Prompt the user or bypass failure if it's missing.
- [x] Review `setup-machine.sh` to ensure Podman installation is either optional or handled gracefully if Homebrew fails to install it (e.g., due to corporate restrictions).

## Phase 3: Documentation and Testing
- [x] Update `GEMINI.md` to reflect the new "Native by Default" architecture.
- [x] Update `conductor/product.md` and `conductor/tech-stack.md`.
- [x] Add or update tests in `tests/test_isolate.py` to verify the new flag behavior.
- [x] Manually verify execution flows: `gemini`, `gemini --sandbox`, and `gemini extension list`.
