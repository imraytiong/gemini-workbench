# Best Practices for Gemini Agentic Environment

This document defines the foundational standards for building, testing, and deploying agents within this workbench. Adherence to these practices ensures safety, reliability, and rapid iteration.

## 1. Architecture & Design (Agentic Core)
*   **Modular Tool Definitions:** Every agent "tool" (Python functions) must have explicit docstrings and JSON-serializable types. Gemini relies on these descriptions for accurate function calling.
*   **Structured Prompting:** Keep prompts separate from code (e.g., in `.prompt` files or YAML). This allows for versioning and non-code prompt engineering iterations.
*   **Context Window Management:** Implement a sliding window or summarization strategy for long-running sessions to prevent performance degradation and high token costs.
*   **Fail-Soft Logic:** Design agents to handle hallucinations or invalid tool outputs gracefully. Use a "Self-Correction" loop where the agent reflects on its own errors before asking the user.

## 2. Development Standards (Python & Gemini)
*   **Strict Type Hinting:** Use Python `typing` and `Pydantic` models for all data structures. This ensures that the data passed between the LLM and your code is strictly validated.
*   **Automated Quality Control:** Enforce `ruff` for linting, `black` for formatting, and `mypy` for static type checking on every save.
*   **Inference Safety:** Use Gemini's built-in safety filters (`HARM_CATEGORY_...`) and implement custom input/output sanitizers for sensitive operations.
*   **Environment Parity:** Always execute code via `gemini-isolate` to ensure the development environment exactly matches the production sandbox.

## 3. Sandbox & Security (Podman)
*   **Zero-Trust Tooling:** Treat any code generated or executed by the agent as untrusted. Run all agent-initiated scripts inside the rootless Podman container.
*   **Volume Mapping Isolation:** Only mount necessary directories into the container. Avoid mounting sensitive host directories (e.g., `~/.ssh`).
*   **Resource Limits:** Set CPU and memory limits on the Podman container to prevent resource exhaustion (OOM) events.
*   **Ephemeral State:** Ensure the agent's workspace is cleaned up between tasks unless persistence is explicitly required for memory.

## 4. Rigorous Testing & Validation
*   **Reproducible Failure States:** Before fixing a bug, you must write a failing test case. This is mandatory for rapid iteration.
*   **LLM-as-a-Judge (Evals):** Use Gemini to evaluate the agent's semantic output. Write tests that ask: *"Did the agent fulfill the intent of the user without violating safety rules?"*
*   **VCR/Mocking for LLM:** Use tools like `vcrpy` to record LLM interactions. This allows for fast, deterministic unit tests that don't cost tokens or require network access.
*   **Integration Benchmarks:** Maintain a "Golden Dataset" of standard queries. Compare the success rate of every major change against this baseline.

## 5. Observability & Iteration
*   **Detailed Trace Logs:** Log every "Thought," "Action," and "Observation" in the agent's loop. Store these in `session_logs/` for post-mortem analysis.
*   **Atomic Changes:** Keep pull requests and changes small (ideally < 50 lines per change).
*   **Auto-Documentation:** Generate documentation from code type hints and docstrings so the agent can "read its own manual" if it gets lost.
