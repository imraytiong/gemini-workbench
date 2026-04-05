# Implementation Plan

## Objective
Finalize the extraction of the `session-logger` skill by updating the workbench's `setup-workbench.sh` to install the new `remember` extension and cleaning up any remaining local references.

## Steps
1. **Update `setup-workbench.sh`**:
   - Add `remember:https://github.com/imraytiong/remember-extension` to the `EXTENSIONS` array in the setup script.
2. **Clean up Documentation**:
   - Search for "session-logger" in `GEMINI.md`, `README.md`, and any other documentation.
   - Replace with "remember" or updated extension information where appropriate.
3. **Verify Installation**:
   - Run `bash setup-workbench.sh --no-build` to ensure the `remember` extension is correctly detected and installed.
