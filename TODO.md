# Gemini Workbench Plan

- [x] **Phase 1: Skill Migration (Project-Aware Logic)**
    - [x] Move the `session-logger` from `~/.gemini/skills/` to `~/projects/gemini-workbench/skills/`.
    - [x] Create a symbolic link from `~/projects/gemini-workbench/skills/session-logger` back to `~/.gemini/skills/session-logger`.
    - [x] Verify that the logger still works correctly from both the host and the sandbox.
- [x] **Phase 2: Build the "Project Scaffolder" Skill**
    - [x] Create a new skill directory: `~/projects/gemini-workbench/skills/project-scaffolder/`.
    - [x] Develop a `scaffold.cjs` script for standardized project creation.
    - [x] Register the skill by symbolically linking it to `~/.gemini/skills/`.
- [x] **Phase 3: Formalize the Agent Development Kit (ADK)**
    - [x] Enter the `gemini-sandbox-container`.
    - [x] Verify `@google/gemini-cli-core` availability.
    - [x] Create a verification script in `gemini-workbench/bin/verify-adk`.

## Status: Complete
The workbench is now a fully-featured development environment with automated project scaffolding and integrated session logging.
