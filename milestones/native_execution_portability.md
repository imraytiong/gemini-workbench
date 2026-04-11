# Milestone: Native Execution & Portability

## Status: NOW
*Current phase of the milestone (NOW, SOON, LATER, COMPLETED).*

## Strategic Objective
Transition the workbench to "Native by Default" to drastically improve portability across corporate environments and reduce developer friction. The Podman sandbox will be retained as an optional, high-security capability rather than a mandatory wrapper.

## Prioritized Tracks
*A list of Conductor tracks needed to fulfill the milestone.*
- [ ] [Transition to Native Default Execution](conductor/tracks/native-default-transition/index.md)

## Success Criteria
*What does "Done" look like?*
- [ ] Running `gemini` natively executes without invoking Podman unless explicitly requested via a flag.
- [ ] The workbench can be fully installed and utilized on a machine without Podman installed.
- [ ] Existing session restoration features continue to work flawlessly in native mode.

## Completed Conductor Tracks
*Historical record of tracks that realized this milestone.*

## Verification Tests
*Tests completed in order to get us to 'Done'.*
