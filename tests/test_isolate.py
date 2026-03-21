import pytest
import subprocess
import os

ISOLATE_PATH = "/Users/raytiongai/projects/gemini-workbench/bin/gemini-isolate"

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
    env_vars = {"GEMINI_CLI": "1", "PATH": f"/Users/raytiongai/projects/gemini-workbench/bin:{os.environ['PATH']}"}
    
    # We use 'ls' because it's in the allowed list for direct execution
    result = run_isolate(["ls"], env_vars=env_vars)
    assert result.returncode == 0
    assert "tests" in result.stdout  # We should see the tests dir in current CWD

def test_isolate_path_translation_dry_run():
    """Verify generated podman command and path translation using DRY_RUN."""
    # Test being in a projects directory
    env_vars = {
        "DRY_RUN": "1",
        "GEMINI_CLI": "0",
        "PODMAN": "echo_podman" # Force use of a specific string to verify
    }
    # Mocking environment to avoid real podman machine start
    # We need to bypass the recursion check
    os.environ["GEMINI_CLI"] = "0"
    os.environ["GEMINI_SANDBOX"] = "0"

    cwd = "/Users/raytiongai/projects/brain"
    result = run_isolate(["python3", "--version"], env_vars=env_vars, cwd=cwd)
    
    # Verify the output contains the translated path
    # Host: /Users/raytiongai/projects/brain
    # Container: /home/raytiongai/projects/brain
    assert "-w /home/raytiongai/projects/brain" in result.stdout
    assert "gemini-sandbox-container python3 --version" in result.stdout

def test_isolate_no_args_defaults_to_gemini():
    """Verify that running without args defaults to starting the gemini interactive mode."""
    env_vars = {"DRY_RUN": "1", "GEMINI_CLI": "0"}
    result = run_isolate([], env_vars=env_vars)
    assert "gemini-sandbox-container gemini" in result.stdout
