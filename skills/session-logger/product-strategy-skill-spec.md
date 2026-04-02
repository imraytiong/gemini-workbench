# 🛡️ Skill Spec: `roadmap-architect`

This document defines the specification for a new Gemini CLI skill that enables a "Strategy-to-Execution" workflow across any project. It bridges the gap between high-level vision and tactical `conductor` tracks.

## 🌟 Core Philosophy
*   **Living Strategy:** The roadmap is not a static artifact but a dynamic view of the "Now," "Soon," and "Later" of a project.
*   **Milestone-Centric:** "Now" capabilities are grouped into discrete Milestones that provide detailed technical justification before work begins.
*   **Fuzzy-to-Fixed:** Strategy is "fuzzy" at the Roadmap level and "fixed" (structured) at the Conductor Track level.

---

## 🛠️ Components & File Structure

### 1. `ROADMAP.md` (The Dashboard)
Located in the project root or `conductor/`.
*   **Phasing:**
    *   **NOW:** Active milestones and imminent capabilities. (Backlinked to `milestones/`)
    *   **SOON:** Priority features and technical debt (1-3 month horizon).
    *   **LATER:** Long-term vision and conceptually "fuzzy" ideas.
*   **Categories:** Capabilities, Infrastructure, Quality of Life, Technical Debt.

### 2. `milestones/` (The Detailed Planning)
A directory containing specific documents for each major release (e.g., `v1.1_semantic_intelligence.md`).
*   **Contents:**
    *   **Strategic Objective:** Why are we doing this?
    *   **Prioritized Tracks:** A list of `conductor` tracks needed to fulfill the milestone.
    *   **Success Criteria:** What does "Done" look like?

---

## 🔄 Workflow & Tools

### `init-roadmap`
Scans the current repo (specifically `backlog.md` if it exists) to create the initial `ROADMAP.md`.

### `create-milestone <name>`
1.  Takes a concept from the "Now" or "Soon" section.
2.  Creates a new Markdown file in `milestones/` with a standard template.
3.  Updates the `ROADMAP.md` to link to this new file.

### `generate-tracks`
1.  Analyzes a chosen Milestone.
2.  Proposes a list of Conductor Tracks.
3.  Upon approval, initializes the folders and `spec.md` files for those tracks in `conductor/tracks/`.

---

## 🧩 Integration with Conductor
This skill acts as the **Pre-Planning Layer** for the existing Conductor framework. 
*   **Strategy Layer:** `ROADMAP.md` ➔ `milestones/`
*   **Execution Layer:** `conductor/tracks/` ➔ `plan.md`

---
*Status: Draft Specification*
*Target: v1.0.0 of Strategy Skill*
