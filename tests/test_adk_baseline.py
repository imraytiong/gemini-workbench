import subprocess
import pytest

def test_adk_baseline_verification(sandbox_ready):
    """Verify the ADK environment is fully operational using the verification script."""
    if not sandbox_ready:
        pytest.skip("Podman sandbox not available or running.")
        
    cmd = ["bin/verify-adk"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    assert result.returncode == 0
    assert "Gemini ADK Verification" in result.stdout
    assert "Sandbox container is active" in result.stdout
    assert "Verification Complete" in result.stdout

def test_hello_world_agent_end_to_end(sandbox_ready):
    """Verify the sample Hello World agent runs successfully in the sandbox."""
    if not sandbox_ready:
        pytest.skip("Podman sandbox not available or running.")
        
    # Use -p flag to run in non-interactive mode
    cmd = ["bin/gemini-isolate", "-p", "run agent in examples/hello-world with input 'test'"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    assert result.returncode == 0
    assert "Hello, World!" in result.stdout
