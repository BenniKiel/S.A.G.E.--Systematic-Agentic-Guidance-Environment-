---
description: An optional step to shape ideas, explore concepts, or build sandboxed Proof of Concepts (PoC) before formal architecture design.
---
# Brainstorm & Proof of Concept Workflow

This workflow provides a safe space for the Agent and User to explore technical ideas, discuss implementation details, or build quick prototypes *outside* the strict C4 architecture rules. 

**Use Cases:**
- Shaping a raw idea further before starting the MVP definition.
- Exploring different implementation approaches for a specific feature.
- Building a quick Proof of Concept (PoC) to see if an API or library actually works.

## Step 1: Open Discussion & Brainstorming
The Agent must first discuss the idea or problem with the User. 
- Weigh different options and trade-offs.
- Avoid forcing an immediate decision. Ask open-ended questions to clarify the vision.
- If the User is looking for purely conceptual shaping, summarize the findings and ask if these should be added to `docs/01_Concept.md` or `docs/02_TechStack.md`.

## Step 2: Safe Prototyping (If requested)
If the User wants to build a PoC or see some actual code to validate an idea:
1. **Strict Sandbox Rule:** All code written during this phase MUST be placed in a dedicated `sandbox/` folder at the root of the project (e.g., `sandbox/auth_poc/`).
2. Do **NOT** modify or add files to the main codebase (`src/`, `lib/`, `docs/systems/`, etc.) during this brainstorm phase.
3. Keep the PoC minimal and focused strictly on answering the outstanding technical question.
4. **Run Instructions:** Provide clear CLI instructions on how the User can run and test the PoC locally (e.g., `cd sandbox/poc && npm install && node server.js`).
5. **Skill Override:** Do **NOT** trigger the `continuous_documentation` or `system_design_standards` skills for sandbox code. PoCs are isolated and must absolutely not pollute the production architecture documentation in `docs/systems/`.
6. **Sandbox Hygiene:** When creating a new PoC folder, immediately add a local `.gitignore` within that folder to prevent committing `node_modules`, build artifacts, or virtual environments.

## Step 3: Conclusion & Transition
Once the brainstorm or PoC has yielded enough clarity:
- **Knowledge Handoff:** Do not let the knowledge die in the chat context! If a major technical decision was made, enforce documenting it via the `/record-decision` workflow (MADR) or adding it to `docs/02_TechStack.md`.
- **Cleanup:** Explicitly ask the User: *"Do you want to keep the Sandbox code for reference, or should I delete it now that we recorded the learnings?"*
- **Next Step:** Recommend the next formal S.A.G.E. step (e.g., `/define-mvp` to ruthlessly scope down the finalized concepts into a Minimum Viable Product).
