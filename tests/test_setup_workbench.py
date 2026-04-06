import pytest
import subprocess
import os
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SETUP_SCRIPT = str(PROJECT_ROOT / "setup-workbench.sh")

def test_setup_workbench_dry_run():
    """
    Test that the setup script runs successfully without actually building the container.
    We pass a mock GEMINI_SANDBOX environment to bypass the podman check if podman isn't installed natively,
    but ensure the script completes its idempotency checks.
    """
    env = os.environ.copy()
    # Mock being in a sandbox so it skips the strict podman requirement 
    # but still executes the symlinking logic.
    env["GEMINI_SANDBOX"] = "1"
    
    result = subprocess.run(
        ["bash", SETUP_SCRIPT, "--no-build"],
        env=env,
        cwd=str(PROJECT_ROOT),
        capture_output=True,
        text=True
    )
    
    # Check that it executed successfully
    assert result.returncode == 0, f"Script failed with output:\n{result.stderr}"
    
    # Verify key steps were announced and completed
    assert "Starting Gemini Workbench setup..." in result.stdout
    assert "Prerequisites met." in result.stdout
    assert "Setting up skills and session log" in result.stdout
    assert "Setup Complete" in result.stdout
