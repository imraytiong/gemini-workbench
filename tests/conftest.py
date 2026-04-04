import pytest
import os
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_env(monkeypatch):
    """Set up a controlled environment for testing CLI wrappers."""
    monkeypatch.setenv("HOME", "/home/testuser")
    monkeypatch.setenv("USER", "testuser")
    # Clear any existing GEMINI_CLI or GEMINI_SANDBOX to test the full path
    monkeypatch.delenv("GEMINI_CLI", raising=False)
    monkeypatch.delenv("GEMINI_SANDBOX", raising=False)

@pytest.fixture
def mock_podman_exec():
    """Globally mock podman calls."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="running", stderr="", returncode=0)
        yield mock_run

@pytest.fixture
def sandbox_ready():
    """Checks if the Podman sandbox is available and running."""
    import subprocess
    try:
        # Check if podman is installed
        subprocess.run(["podman", "--version"], capture_output=True, check=True)
        # Check if container is running
        result = subprocess.run(["podman", "ps", "--format", "{{.Names}}"], capture_output=True, text=True, check=True)
        if "gemini-sandbox-container" in result.stdout:
            return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        pass
    return False
