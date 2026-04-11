# Technology Stack: Gemini Workbench

## Languages
- **Bash (Shell):** Primary scripting language for host-machine automation and CLI wrappers.
- **Node.js:** Core runtime for the Gemini CLI and its associated skill development.
- **Python:** Primary language for project-level testing and automation scripts.

## Frameworks & Tools
- **Podman:** Optional containerization engine providing full Ubuntu-based environment isolation for high-risk agentic tasks.
- **Gemini CLI:** The central tool that the workbench is built to support and extend.
- **ADK (Agent Development Kit):** Used for building sophisticated AI agents within the workbench.

## Testing & Quality
- **Pytest:** Python-based testing framework for validating workbench tools and isolated containers.
- **Bash Automated Testing:** Used for verifying host-side shell scripts and configuration.

## Environment & Infrastructure
- **Operating System:** Ubuntu (containerized), macOS/Linux (host).
- **Isolation Layer:** Podman containers for isolated execution.
- **Logging:** Local session logging to the `session_logs/` directory.
