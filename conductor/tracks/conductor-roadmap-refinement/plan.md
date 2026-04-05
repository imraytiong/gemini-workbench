# Track Plan: Conductor Roadmap Refinement and Alignment

## Phase 1: Milestone Migration
- [ ] Migrate `roadmap_architect.md` to `conductor_roadmap_flow.md` or similar (since the skill is renamed).
- [ ] Update `release_1_1.md` with status `SOON` and estimated timestamps.
- [ ] Update `portable_safety_policies.md` with status `NOW` and estimated timestamps.
- [ ] Update `podman_auto_recovery.md` with status `LATER` and estimated timestamps.

## Phase 2: Track Cleanup
- [ ] Audit `conductor/tracks/roadmap-architect` and merge/delete it since `conductor-roadmap-flow` is now the canonical track.
- [ ] Update `conductor/tracks/` metadata files to use consistent naming.

## Phase 3: Final Verification
- [ ] Run `promote_milestone.cjs` on all milestones to ensure they are in the correct `ROADMAP.md` sections.
- [ ] Verify reverse-chronological order in `COMPLETED`.
- [ ] Final project-wide check of references to `roadmap-architect`.
