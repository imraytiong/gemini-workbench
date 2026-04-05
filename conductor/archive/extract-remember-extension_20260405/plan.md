# Implementation Plan

## Objective
Extract the `session-logger` skill from `gemini-workbench` and package it as a standalone Gemini CLI extension named `remember`.

## Steps
1. **Create Directory Structure**:
   - Create a new project directory at `../remember-extension`. (Confirmed writable)
   - Set up the extension scaffolding (`skills/remember`, `README.md`, `gemini-extension.json`).
2. **Migrate Skill Code**:
   - Copy `SKILL.md` and `scripts/log_session.cjs` from `gemini-workbench/skills/session-logger` to `../remember-extension/skills/remember`.
3. **Refactor Identifiers**:
   - Rename internal references from `session-logger` to `remember` in the skill's markdown and scripts if necessary.
   - Update `gemini-extension.json` with appropriate metadata.
4. **Validation**:
   - Install the extension locally via `gemini extension install ../remember-extension --consent`.
   - Verify the extension appears in `gemini extension list`.
