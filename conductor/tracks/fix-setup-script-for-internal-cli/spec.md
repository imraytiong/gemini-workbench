# Spec: Fix Setup Script for Internal Gemini CLI

**Objective:** Modify `setup-workbench.sh` to reliably detect and use the Google-internal Gemini CLI, which is often configured as a shell alias rather than a command in the system's PATH.

## 1. Problem Statement

The `setup-workbench.sh` script currently checks for the `gemini` command using `command -v gemini`. This check fails in development environments where `gemini` is an alias (e.g., aliased to `<internal-gemini-path>`).

Aliases are typically only resolved in interactive shells. When the setup script runs, it executes in a non-interactive shell where the `gemini` alias is not available. This causes the script to incorrectly report that the Gemini CLI is not installed, blocking the setup process for users with this standard configuration.

## 2. Success Criteria

- The `setup-workbench.sh` script must be updated to no longer rely on `command -v gemini`.
- The script must successfully locate and use the hard-coded path for the internal Gemini CLI: `<internal-gemini-path>`.
- The script must check if this specific executable exists and is runnable.
- All calls to `gemini` within the script must be replaced with the full path.
- A test will be created to validate that the script runs without errors in a simulated non-interactive environment.
- The final script must remain executable and pass the new test.
