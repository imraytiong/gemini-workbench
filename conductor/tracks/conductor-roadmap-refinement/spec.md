# Track Specification: Conductor Roadmap Refinement and Alignment

## Vision
Standardize all existing milestones and conductor tracks to the new `conductor-roadmap` format. This ensures a consistent project history and clear status tracking across all work.

## Goals
- **Milestone Standardization**: Update all existing milestones with the new status and timestamp fields.
- **Track Consistency**: Align track names and references with the renamed `conductor-roadmap` skill.
- **Data Integrity**: Ensure every milestone and track has accurate status and historical records.

## Scope
- [ ] Migrate `milestones/roadmap_architect.md` to the new format.
- [ ] Migrate `milestones/release_1_1.md` to the new format.
- [ ] Migrate `milestones/portable_safety_policies.md` to the new format.
- [ ] Migrate `milestones/podman_auto_recovery.md` to the new format.
- [ ] Rename/Cleanup `conductor/tracks/roadmap-architect` (it's redundant with `conductor-roadmap-flow`).
- [ ] Update all track indices to point to the correct milestone identifiers.
- [ ] Verify that all milestones in `ROADMAP.md` correctly reflect their current state.

## User Requirements
- Rough date stamp plus the hour of the day for all milestones.
- Ensure all tracks are correctly categorized and linked.
