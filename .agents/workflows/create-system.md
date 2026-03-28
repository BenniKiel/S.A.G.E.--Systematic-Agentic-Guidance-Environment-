---
description: Creates a new system with proper interface documentation.
---
# Create System Workflow

This workflow creates a new system with a rigorous focus on design and clear component boundaries.

**Prerequisites:** 
- The user has requested a new system (e.g., "Quest System", "Economy System").
- `docs/` structure is already initialized.

## Step 1: Research & Setup
Read the relevant core concepts in `docs/` (`01_Concept.md` and `02_TechStack.md`). If the requested system interacts with existing systems, read their docs in `docs/systems/` as well.

## Step 2: Documentation drafting (Concept phase)
Create the system documentation file in `docs/systems/<System_Name>.md`. 
**CRITICAL:** You MUST strictly follow the `system_design_standards` template (Component Overview, Architecture Diagram, Public Interfaces, Dependencies, Data Structures, Known Limitations, Testing & Verification).

## Step 3: Architecture Review
Stop and refer the user to the new `docs/systems/<System_Name>.md` document.
> *"Ich habe das C4-Design für das System entworfen. Wenn du das Design absegnest, starte ich mit dem Coding!"*

**CRITICAL NOTE FOR AGENT (The Build Loop & QA Gate):** 
Der reine `/create-system` Workflow (Architektur) endet hier. Sobald der Nutzer das "Go" für das Coding gibt, arbeitest du normal weiter. 
**NACHDEM** du den Code fertig geschrieben hast, führst du zwingend das QA-Gate aus:
1. **QA Gate:** Zwinge den User zum lokalen Test (`npm run dev` o.Ä.).
2. **Check-Off:** Erst wenn der User den Erfolg bestätigt, öffnest du `docs/systems/_System_Roadmap.md` und setzt einen Haken `[x]` bei dem System.
3. **The Handoff:** Danach fragst du: *"Sollen wir nun mit System N+1 auf der Liste weitermachen (`/create-system [Name]`), oder sind alle Systeme fertig und wir schließen das Projekt ab (`/wrap-mvp`)?"*
