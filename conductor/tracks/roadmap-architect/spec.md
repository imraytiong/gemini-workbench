# Track Specification: `roadmap-architect` Skill

This specification defines the roadmap-architect skill for Gemini CLI, enabling a Strategy-to-Execution workflow.

## Vision
A dynamic project roadmap that bridges high-level vision and tactical execution through discrete milestones and automated track generation.

## Components
### `ROADMAP.md` (The Dashboard)
Located in project root or `conductor/`.
- NOW: Active milestones and imminent capabilities.
- SOON: Priority features and tech debt.
- LATER: Long-term vision and conceptually "fuzzy" ideas.

### `milestones/` (Detailed Planning)
Markdown files for each milestone (e.g., `milestones/v1.0.md`).
- Contents: Strategic Objective, Prioritized Tracks, Success Criteria.

## Tools & Commands
- `init-roadmap`: Create initial `ROADMAP.md` from `backlog.md`.
- `create-milestone <name>`: Create a new milestone document.
- `generate-tracks`: Propose and create Conductor tracks from a milestone.
