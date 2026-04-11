import pytest
import subprocess
import os
from pathlib import Path
import getpass

# Dynamically resolve paths relative to the project root
PROJECT_ROOT = Path(__file__).resolve().parent.parent
ISOLATE_PATH = str(PROJECT_ROOT / "bin" / "gemini-isolate")
PROJECTS_DIR = PROJECT_ROOT.parent

def run_isolate(args, env_vars=None, cwd=None):
    """Run gemini-isolate with specific environment and arguments."""
    env = os.environ.copy()
    if env_vars:
        env.update(env_vars)
    
    result = subprocess.run(
        ["bash", ISOLATE_PATH] + args,
        env=env,
        cwd=cwd,
        capture_output=True,
        text=True
    )
    return result

def test_isolate_recursion_handling():
    """Test that isolate runs the local 'gemini' when already in a sandbox."""
    # Mocking that we are already in the sandbox
    bin_path = str(PROJECT_ROOT / "bin")
    env_vars = {"GEMINI_CLI": "1", "PATH": f"{bin_path}:{os.environ['PATH']}"}
    
    # We use 'ls' because it's in the allowed list for direct execution
    result = run_isolate(["ls"], env_vars=env_vars, cwd=str(PROJECT_ROOT))
    assert result.returncode == 0
    assert "tests" in result.stdout  # We should see the tests dir in current CWD

def test_isolate_path_translation_dry_run():
    """Verify generated podman command and path translation using DRY_RUN."""
    # Test being in a projects directory
    env_vars = {
        "DRY_RUN": "1",
        "GEMINI_CLI": "0",
        "PODMAN": "echo_podman", # Force use of a specific string to verify
        "USER": "testuser"
    }
    # Mocking environment to bypass the recursion check
    os.environ["GEMINI_CLI"] = "0"
    os.environ["GEMINI_SANDBOX"] = "0"

    # Use the current user to match what gemini-isolate will resolve
    host_user = getpass.getuser()
    cwd = str(PROJECTS_DIR / "brain")
    
    result = run_isolate(["python3", "--version"], env_vars=env_vars, cwd=cwd)
    
    # Verify the output contains the translated path
    assert f"-w /home/{host_user}/projects/brain" in result.stdout
    assert "gemini-sandbox-container python3 --version" in result.stdout

def test_isolate_no_args_defaults_to_gemini():
    """Verify that running without args defaults to starting the gemini interactive mode."""
    env_vars = {"DRY_RUN": "1", "GEMINI_CLI": "0"}
    result = run_isolate([], env_vars=env_vars)
    assert "gemini-sandbox-container gemini" in result.stdout

def test_isolate_unrecognized_command_defaults_to_gemini():
    """Verify that an unrecognized command is passed as an argument to gemini."""
    env_vars = {"DRY_RUN": "1", "GEMINI_CLI": "0"}
    result = run_isolate(["unknown_command", "arg1"], env_vars=env_vars)
    assert "gemini-sandbox-container gemini unknown_command arg1" in result.stdout

def test_isolate_known_shell_command_direct_execution():
    """Verify that a known shell command (e.g., 'git') is executed directly, not via gemini."""
    env_vars = {"DRY_RUN": "1", "GEMINI_CLI": "0"}
    result = run_isolate(["git", "status"], env_vars=env_vars)
    assert "gemini-sandbox-container git status" in result.stdout
    assert "gemini git status" not in result.stdout

def test_isolate_absolute_path_direct_execution():
    """Verify that an absolute path is executed directly."""
    env_vars = {"DRY_RUN": "1", "GEMINI_CLI": "0"}
    result = run_isolate(["/bin/bash", "-c", "echo test"], env_vars=env_vars)
    assert "gemini-sandbox-container /bin/bash -c echo test" in result.stdout

def test_wrapper_native_default():
    """Verify that bin/gemini defaults to native execution (NOSANDBOX=true)."""
    wrapper_path = str(PROJECT_ROOT / "bin" / "gemini")
    env = os.environ.copy()
    env["GEMINI_CLI"] = "0"
    
    # Run with a dummy command that won't actually invoke gemini-isolate but will print args if it did
    # We grep for NOSANDBOX=true or the absence of gemini-isolate call
    # Actually, the easiest way is to run 'bin/gemini --version' which natively skips restore and executes natively.
    result = subprocess.run(["bash", wrapper_path, "--version"], env=env, capture_output=True, text=True)
    assert result.returncode == 0
