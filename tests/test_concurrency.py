import os
import subprocess
import threading
import time
import pytest
import shutil

# Path to the log script
LOG_SCRIPT = os.path.expanduser("~/.gemini/extensions/remember/skills/remember/scripts/log_session.cjs")

def run_log_session(title, summary, next_steps, cwd, plan="", outcome=""):
    env = os.environ.copy()
    env["GEMINI_GLOBAL_LOG_ROOT"] = str(cwd)
    cmd = [
        "node",
        os.path.join(os.getcwd(), LOG_SCRIPT),
        title,
        summary,
        next_steps,
        plan,
        outcome
    ]
    result = subprocess.run(
        cmd, capture_output=True, text=True, cwd=cwd, env=env
    )
    return result

def test_concurrent_logging(tmp_path):
    # Initialize a git repo in tmp_path
    subprocess.run(["git", "init"], check=True, cwd=tmp_path)
    subprocess.run(["git", "config", "user.email", "test@example.com"], check=True, cwd=tmp_path)
    subprocess.run(["git", "config", "user.name", "Test User"], check=True, cwd=tmp_path)
    
    # Create the session_log directory
    (tmp_path / "session_log").mkdir()
    
    num_threads = 5
    threads = []
    
    results = []
    def worker(i):
        res = run_log_session(f"Title {i}", f"Summary {i}", f"Next Steps {i}", cwd=tmp_path)
        results.append(res)

    for i in range(num_threads):
        t = threading.Thread(target=worker, args=(i,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    for res in results:
        if res.returncode != 0:
            print(f"STDOUT: {res.stdout}")
            print(f"STDERR: {res.stderr}")
            assert res.returncode == 0, f"Log session failed with return code {res.returncode}"
        
    # Check the history file
    history_file = tmp_path / "session_log" / "session-history.md"
    assert history_file.exists()
    
    content = history_file.read_text()
    
    # Count how many titles are present
    for i in range(num_threads):
        assert f"Title {i}" in content, f"Title {i} missing from history"

if __name__ == "__main__":
    # For manual testing
    test_concurrent_logging(pytest.Path.cwd() / "tmp_test")
