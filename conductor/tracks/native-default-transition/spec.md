# Track Specification: Transition to Native Default Execution

## Vision
To make the Gemini Workbench highly portable and reduce execution overhead by defaulting to native host execution, while retaining the Podman sandbox as an optional security layer for high-risk agentic tasks.

## Goals
- **Default to Native:** The `bin/gemini` wrapper must default to executing the native Gemini CLI binary.
- **Opt-in Sandbox:** Introduce a `--sandbox` (or `-s`) flag to manually invoke `bin/gemini-isolate`.
- **Decoupled Setup:** Ensure `setup-workbench.sh` and `setup-machine.sh` do not fail if Podman is absent.
- **Documentation Alignment:** Update project documentation to reflect this architectural shift.

## Anti-Goals
- We are *not* removing the sandbox entirely or deleting `gemini-isolate`.
- We are *not* changing how extensions or projects bypass sandboxing (they already execute natively).
