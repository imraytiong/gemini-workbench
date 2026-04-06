# Plan: Fix Setup Script for Internal Gemini CLI

This plan outlines the steps to diagnose, fix, and verify the `setup-workbench.sh` script to ensure it works with the Google-internal Gemini CLI alias.

## 1. Revert Previous Changes

To ensure this track is a self-contained, idempotent operation, we will first revert the manual changes that were previously applied to `setup-workbench.sh`.

- **Action:** Use `git restore` to revert the file to its original state (pre-modification).

## 2. Create a Test to Reproduce the Failure

We will create a temporary test script that executes `setup-workbench.sh` in a non-interactive environment and confirms that it fails as expected.

- **Action:** Create a new executable file: `test_setup.sh`.
- **Content:** The script will run `setup-workbench.sh` and check for the specific error message "Error: gemini is not installed."

## 3. Confirm the Failure

Execute the test script to ensure it fails correctly. This validates that our test accurately captures the problem.

- **Action:** Run `bash test_setup.sh`.
- **Expected Outcome:** The script should exit with a success code, indicating that it found the error message.

## 4. Implement the Fix

Modify `setup-workbench.sh` to use the hard-coded path for the Gemini CLI.

- **Action 1:** Define a variable `GEMINI_EXEC` pointing to `<internal-gemini-path>`.
- **Action 2:** Replace the generic `command -v gemini` check with a check for the existence and executability of `$GEMINI_EXEC`.
- **Action 3:** Replace all subsequent calls from `gemini` to `$GEMINI_EXEC`.

## 5. Verify the Fix

Re-run the test script. This time, it should fail because the error message it's looking for is no longer produced. We will then modify the test to check for a successful run.

- **Action 1:** Run `bash test_setup.sh` again.
- **Expected Outcome 1:** The test should now fail, as the "gemini is not installed" error is gone.
- **Action 2:** Modify `test_setup.sh` to check for a successful completion message from the setup script (e.g., "Setup Complete").
- **Action 3:** Run the modified `test_setup.sh`.
- **Expected Outcome 2:** The test should pass, confirming the setup script ran successfully.

## 6. Cleanup

Remove the temporary test script.

- **Action:** Delete `test_setup.sh`.
