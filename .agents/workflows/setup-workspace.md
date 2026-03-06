---
description: Scaffolds the initial `docs/` structure: Concept, Tech Stack, Systems.
---
# Setup Workspace Workflow

This workflow initializes the core documentation architecture according to the `continuous_documentation` and `system_design_standards` skills.

1. Create a `docs/` directory in the root of the workspace.
// turbo
2. Create `docs/01_Concept.md` with a template for the high-level design, vision, and fundamental design decisions.
// turbo
3. Create `docs/02_TechStack.md` with a template for used technologies, frameworks, and important links.
// turbo
4. Create `docs/systems/` directory.
// turbo
5. Create `docs/systems/README.md` containing an index of all systems and summarizing the system design standards.
// turbo
6. Create `docs/decisions/` directory.
// turbo
7. Create `docs/decisions/0001-record-architecture-decisions.md` documenting the decision to use MADR for all future architectural decisions (following the `architecture_decision_records` skill).

**Execution Notes for the Agent:**
- When running this workflow, use your terminal tools (`run_command`) or file creation tools (`write_to_file`) to generate the files and directories described above.
- Ensure the templates you use are detailed enough to give the user a clear starting point.
