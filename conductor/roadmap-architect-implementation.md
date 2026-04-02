# Implementation Plan: `roadmap-architect` Skill

This plan outlines the steps to build and integrate the `roadmap-architect` skill into the Gemini Workbench.

## Objective
Build the `roadmap-architect` skill as defined in `product-strategy-skill-spec.md` to bridge the gap between high-level project strategy and tactical Conductor tracks.

## Key Files & Context
- **Spec**: `product-strategy-skill-spec.md`
- **Skill Location**: `skills/roadmap-architect/`
- **Conductor Track**: `conductor/tracks/roadmap-architect/`

## Implementation Plan

### Phase 1: Track Setup & Scaffolding
- [ ] Create Conductor track directory: `conductor/tracks/roadmap-architect/`
- [ ] Initialize track files: `index.md`, `spec.md`, `plan.md`, `metadata.json`
- [ ] Register track in `conductor/tracks.md`
- [ ] Initialize skill using `init_skill.cjs`: `node /opt/homebrew/lib/node_modules/@google/gemini-cli/bundle/builtin/skill-creator/scripts/init_skill.cjs roadmap-architect --path ./skills`

### Phase 2: Templates & Documentation
- [ ] Create `skills/roadmap-architect/references/roadmap-template.md`
- [ ] Create `skills/roadmap-architect/references/milestone-template.md`
- [ ] Update `skills/roadmap-architect/SKILL.md` with comprehensive instructions and metadata.

### Phase 3: Script Implementation
- [ ] Implement `skills/roadmap-architect/scripts/init_roadmap.cjs`: Scans repo for `backlog.md` and creates `ROADMAP.md`.
- [ ] Implement `skills/roadmap-architect/scripts/create_milestone.cjs`: Creates a milestone file from template.
- [ ] Implement `skills/roadmap-architect/scripts/generate_tracks.cjs`: Analyzes milestone and proposes Conductor tracks.

### Phase 4: Testing & Packaging
- [ ] Create a test project environment to verify skill functionality.
- [ ] Run `init-roadmap` and verify output.
- [ ] Run `create-milestone` and verify output.
- [ ] Run `generate-tracks` and verify output.
- [ ] Package the skill: `node /opt/homebrew/lib/node_modules/@google/gemini-cli/bundle/builtin/skill-creator/scripts/package_skill.cjs ./skills/roadmap-architect`
- [ ] Install the skill: `gemini skills install ./skills/roadmap-architect.skill --scope workspace`

## Verification & Testing
- **Manual Verification**:
  1. Initialize a new roadmap in a test folder.
  2. Create a "v1.0" milestone.
  3. Generate tracks from the milestone and ensure they appear in `conductor/tracks/`.
- **Automated Verification**:
  - Add unit tests for the scripts in `skills/roadmap-architect/tests/` (if applicable) or verify via a test runner script.
