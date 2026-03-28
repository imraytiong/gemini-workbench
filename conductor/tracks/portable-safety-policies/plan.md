# Implementation Plan: Portable Safety Policies

## Tasks
1. [x] **Restructure Workbench:**
   - [x] Create `policies/` directory in root.
   - [x] Move `relaxed-safety.toml` to `policies/`.
   - [x] Delete temporary `.gemini/` workspace directory.
2. [x] **Update Setup Script:**
   - [x] Modify `setup-workbench.sh` to include a new step for symlinking policies from `policies/` to `$HOME/.gemini/policies/`.
3. [x] **Execution:**
   - [x] Run the updated `setup-workbench.sh`.
4. [x] **Validation:**
   - [x] Verify symlink exists in `$HOME/.gemini/policies/`.
   - [x] Test a safe command to verify auto-approval (if safe to do so).
