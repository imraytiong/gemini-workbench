# Milestone: Release 1.1 - Open Source & Team Readiness

## Strategic Objective
Transition the Gemini Workbench from a private, personal utility into a safe, easily installable, robust, and open-source tool ready for public GitHub release. This involves sanitizing private data, establishing community governance, ensuring idiomatic Gemini CLI integration, and stabilizing the core experience by removing flaky features.

## Prioritized Tracks
*Tracks needed to fulfill this milestone (to be generated via Roadmap Architect):*

- [ ] **Privacy & Security Sanitization**: Audit and remove hardcoded personal paths (e.g., `/Users/raytiongai`), private keys, and configure strict `.gitignore`/`.geminiignore` boundaries.
- [ ] **Streamlined Onboarding & Installation**: Refactor setup scripts for automatic dependency management and ensure the workbench operates via idiomatic Gemini CLI mechanisms.
- [ ] **Dual-Audience Documentation**: Create a comprehensive `README.md` for human operators and optimize `GEMINI.md`/`product.md` for AI agent comprehension.
- [ ] **Quality Assurance & CI/CD**: Increase test coverage for core scripts, fix bugs, and implement GitHub Actions to automatically test PRs.
- [ ] **Remove Flaky Podman Recovery**: Strip out `bin/sandbox-reset`, `commands/sandbox/reset.toml`, and related auto-recovery logic from `bin/gemini-isolate` to prevent user confusion.
- [ ] **Community & Governance**: Add `LICENSE` (e.g., MIT/Apache), `CONTRIBUTING.md`, `SECURITY.md`, Code of Conduct, and GitHub Issue/PR templates.
- [ ] **Polished Examples**: Update `examples/hello-world/` to serve as the gold standard for usage.

## Success Criteria
- [ ] The project can be cloned and fully installed on a fresh machine seamlessly.
- [ ] Zero private keys, hardcoded paths, or sensitive data exist in the codebase.
- [ ] The repository includes a valid open-source License, Contributing guidelines, and Security policy.
- [ ] GitHub Actions run tests automatically on new PRs.
- [ ] The workbench is provided to the user using idiomatic Gemini CLI integration methods.
- [ ] Flaky Podman auto-recovery code has been completely removed.
- [ ] Documentation is highly readable for both developers and their Gemini CLI agents.
