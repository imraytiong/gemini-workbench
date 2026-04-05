# Track Specification: Conductor Roadmap Extension Scaffolding

## Vision
Transform the `conductor-roadmap` skill into a standalone, installable Gemini CLI extension that anyone can use. This includes providing high-level slash commands for a seamless user experience.

## Goals
- **Standalone Distribution**: Package the skill so it can be installed via a single `gemini extensions install` command.
- **Slash Command Integration**: Provide `/roadmap:init`, `/roadmap:create`, and `/roadmap:promote` commands.
- **Documentation**: Create a comprehensive `README.md` explaining how to use the extension.

## Scope
- [ ] Create `conductor-roadmap-extension/` directory.
- [ ] Generate `gemini-extension.json` manifest.
- [ ] Create `commands/roadmap/` with TOML files for each slash command.
- [ ] Move the `conductor-roadmap` skill into the extension's `skills/` directory.
- [ ] Provide instructions for the user to push to GitHub and install.

## User Requirements
- Installable via GitHub.
- Slash commands for the primary roadmap operations.
- Dependency check for Conductor must remain intact.
