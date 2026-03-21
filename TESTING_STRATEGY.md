# 🛡️ Agentic Testing & Validation Strategy (ATVS)

This document defines the mandatory testing protocols for all agentic development within this workbench. Adherence to these standards ensures that our automated systems remain safe, deterministic, and high-performance.

## 1. The "Guardian" Loop (Mandatory Workflow)
Every code modification must follow this non-negotiable lifecycle:
1.  **Baseline Run:** Execute the `Fast` test suite *before* any change. If tests fail, the environment is unstable; stop and report.
2.  **Intent Disclosure:** If a change requires modifying an existing test or adding a new one, the **Test Change Intent** must be presented to the user for explicit approval.
3.  **Surgical Act:** Apply the code modification.
4.  **Post-Check:** Re-run the test suite.
5.  **Conflict Resolution:** If a test fails, provide a **Failure Analysis** and a **Recommended Path** (Fix Code vs. Update Test). The user makes the final call.

## 2. Test Categorization (Pytest Markers)
To maintain a fast development rhythm, tests are categorized by speed and dependency:

*   **⚡ Fast (`pytest -m "not slow"`):** Unit tests, string manipulations, and mocked logic. Target: **< 2 seconds**.
*   **⏳ Slow (`pytest -m "slow"`):** Integration tests involving disk I/O, mocked API recordings (VCR), or container overhead.
*   **🧠 Eval (`pytest -m "eval"`):** LLM-as-a-Judge semantic validations. These are token-intensive and used for quality benchmarking.

## 3. Data Safety & "Production" Isolation
Tests MUST NEVER modify real user data or state.
*   **Isolation:** All tests use `pytest` fixtures that redirect data paths to a temporary directory (`tmp_path`).
*   **Git Mocks:** `subprocess.run(["git", ...])` is globally mocked in the test suite to prevent accidental commits to production repositories.
*   **No-Network:** `Fast` tests are strictly forbidden from making network calls.

## 4. Multi-Layered ADK Strategy
The **Agent Development Kit (ADK)** requires specialized validation:
*   **Path Parity:** Verify host-to-container path translation logic without starting a container.
*   **Permission Check:** Ensure `UID/GID` mapping is consistent across different host environments (e.g., Mac Mini vs. MacBook).
*   **Sandbox Integrity:** A periodic "Pulse Check" verifies that the Podman socket and volume mounts are operational.

## 5. Decision Framework for Failures
When a decision is required from the user, the agent will provide:
1.  **Trace:** What exactly failed.
2.  **Root Cause:** Is it a **Regression** (unintended breakage) or a **Contract Change** (code evolved correctly, test is stale)?
3.  **Recommendation:** A clear "Fix Code" or "Update Test" suggestion with technical justification.

---
*Last Updated: 2026-03-21*
