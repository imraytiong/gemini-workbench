# Specification: Portable Safety Policies

## Goal
The goal is to centralize Gemini CLI safety policies in the `gemini-workbench` repository to make them portable, version-controlled, and globally applicable via the standard setup process.

## Requirements
1. **Centralization:** Move safety policies from the hidden `.gemini/` folder to a root-level `policies/` directory.
2. **Global Application:** Update `setup-workbench.sh` to automatically symlink policies from the workbench to `$HOME/.gemini/policies/`.
3. **Safety Balance:** Relax read-only and safe shell operations while maintaining strict manual approval for destructive operations like `rm` and `git rm`.

## Scope
- `policies/` directory in workbench root.
- `setup-workbench.sh` modification.
- Removal of temporary `.gemini/` directory in the workbench.
