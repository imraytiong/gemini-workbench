# Release 1.1 - Open Source & Team Readiness

## Overview
Release 1.1 marks the transition of Gemini Workbench from a private utility to a safe, easily installable, and open-source-ready developer environment.

## Key Changes
- **Security & Sanitization**: Removed all hardcoded personal paths (e.g., `/Users/raytiongai`) and untracked sensitive local session logs from Git.
- **Improved Installation**: `setup-workbench.sh` is now fully idempotent, supports dependencies prompts, and includes a `--no-build` flag for faster local iteration.
- **Open-Source Foundations**: 
    - Added Apache 2.0 License.
    - Added comprehensive contributing guidelines and security policies.
    - Added GitHub issue/PR templates.
- **Stability**: Removed flaky Podman auto-recovery scripts to ensure reliable sandbox orchestration.

## Getting Started
See the [README.md](README.md) for full installation and usage documentation.
