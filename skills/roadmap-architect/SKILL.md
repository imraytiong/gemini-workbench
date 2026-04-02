---
name: roadmap-architect
description: Bridging strategy and execution by managing project roadmaps and milestones. Use when you need to define high-level project goals, create strategic milestones, and generate tactical Conductor tracks.
---

# Roadmap Architect

This skill manages the **Strategy-to-Execution** workflow for any project. It centers around a `ROADMAP.md` file and discrete milestone documents.

## Workflow

### 1. Initialize Roadmap
Run `init-roadmap` to scan the current repository (and `backlog.md` if available) and generate the initial `ROADMAP.md`.

### 2. Create Milestone
Run `create-milestone <name>` to define a specific strategic goal from the Roadmap. This creates a detailed document in `milestones/` using the [milestone-template.md](references/milestone-template.md).

### 3. Generate Tracks
Run `generate-tracks <track-id> [track-title]` to initialize a tactical **Conductor Track**. This initializes the folder structure and registers it in `conductor/tracks.md`.

## Components

- **ROADMAP.md**: High-level phasing (NOW, SOON, LATER) and categorization.
- **milestones/**: Discrete technical and strategic justifications.
- **Conductor Tracks**: Tactical execution plans (bridged automatically from milestones).

## References
- [ROADMAP Template](references/roadmap-template.md)
- [Milestone Template](references/milestone-template.md)
