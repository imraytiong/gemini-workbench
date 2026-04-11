# Product Guide: Gemini Workbench

## Vision
To provide a comprehensive, ready-to-use development environment for maximizing the effectiveness of the Gemini CLI. It streamlines the initial setup process, offering a "workshop-in-a-box" experience that includes pre-configured tools, settings, and skills, allowing developers to immediately focus on building high-quality AI agents.

## Key Goals
- **Rapid Onboarding:** Minimize initial configuration time for the Gemini CLI and its associated development tools.
- **Agentic Workshop:** Provide a curated set of common tools, settings, and baseline skills to jumpstart agent development.
- **ADK Focus:** Prioritize initial development workflows for building agents using the Agent Development Kit (ADK).
- **Expandability:** Design the workbench to easily accommodate new skills, tools, and custom CLI extensions.
- **Optional Isolation:** Ensure consistent and isolated development environments through containerization when required for security or consistency. Native execution is the default for maximum portability.

## Target Audience
- Developers building AI agents with the Gemini CLI and ADK.
- Software engineers who want a pre-configured workshop for agentic development.

## Core Features
- `gemini-isolate`: Podman-based environment isolation for consistent agent execution.
- `setup-workbench.sh`: Automated host-machine configuration and tool-chain initialization.
- **Toolbox:** Integrated wrappers (`bin/`) for common Gemini CLI operations.
- **Skill Repository:** Centralized management and symlinking of agent skills.
- **ADK Support:** Optimized workflows for building and testing ADK-based agents.
