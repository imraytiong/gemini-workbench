# Implementation Plan

## Objective
Automate the installation of Conductor and Conductor Roadmap extensions during workspace setup, and ensure all extension management commands bypass sandboxing by default.

## Steps
1. **Update `setup-workbench.sh`**:
   - Add commands to install `conductor` and `conductor-roadmap` extensions if they are not already installed.
2. **Update `bin/gemini`**:
   - Modify the argument parsing loop to detect the `extension` subcommand.
   - When the `extension` subcommand is present, automatically set `NOSANDBOX=true` and `SKIP_RESTORE=true`.
3. **Validate**:
   - Ensure the modifications in `bin/gemini` are robust and correctly pass arguments to the native gemini binary.
   - Check `setup-workbench.sh` for syntax correctness.
