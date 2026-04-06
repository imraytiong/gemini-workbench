# Track Plan: Streamlined Onboarding & Installation

## Phase 1: Automation & Dependency Handling
- [x] Audit `setup-workbench.sh` for non-idempotent operations and dependency checks.
- [x] Implement friendly installation prompts for missing dependencies instead of `exit 1`.
- [x] Add idempotency checks for `gemini project add` and `git config --global`.

## Phase 2: Refactoring
- [x] Introduce a `--no-build` flag for `setup-workbench.sh` to skip unnecessary sandbox image rebuilds.
- [x] Standardize environment detection and provide clearer setup status output.
