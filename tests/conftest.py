import pytest
import os
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_env(monkeypatch):
    """Set up a controlled environment for testing CLI wrappers."""
    monkeypatch.setenv("HOME", "/Users/raytiongai")
    monkeypatch.setenv("USER", "raytiongai")
    # Clear any existing GEMINI_CLI or GEMINI_SANDBOX to test the full path
    monkeypatch.delenv("GEMINI_CLI", raising=False)
    monkeypatch.delenv("GEMINI_SANDBOX", raising=False)

@pytest.fixture
def mock_podman_exec():
    """Globally mock podman calls."""
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="running", stderr="", returncode=0)
        yield mock_run
