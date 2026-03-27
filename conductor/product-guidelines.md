# Product Guidelines: Gemini Workbench

## Prose Style
- **Tone:** Technical, direct, and concise.
- **Voice:** Professional and objective.
- **Rules:**
  - Prioritize technical rationale over conversational filler.
  - Use clear, active voice for documentation and instructions.

## UX Principles
- **CLI-First Efficiency:** All workbench tools and wrappers must prioritize high-signal output and command-line efficiency.
- **Transparent & Audit-Ready:** Every session and significant action must be logged for full observability.
- **Frictionless Automation:** Automate all repetitive configuration and execution tasks to minimize developer friction.

## Quality & Testing
- **Regression Prevention:** Prioritize the prevention of regressions through comprehensive test coverage.
- **Fast Feedback Loops:** Every feature and capability must include fast, automated tests to ensure continuous stability.
- **Bug Verification:** Every reported bug must be accompanied by a reproduction test case to verify the fix and prevent future occurrences.

## Design Aesthetic
- **Minimalist Core:** Clean, focused, and free of redundant "just-in-case" alternatives.
- **Functional Clarity:** Prioritize clear, informative error messages and progress indicators.

## Code & Structure
- **Modular Design:** New tools and skills should be designed as independent, pluggable components.
- **Isolated Execution:** Adhere to the core mandate of full Podman isolation for all workbench-related code execution.
