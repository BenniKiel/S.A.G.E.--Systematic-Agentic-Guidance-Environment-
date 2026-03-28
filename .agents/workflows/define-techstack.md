---
description: Defines the global technical architecture and tech stack based on the MVP before designing individual systems.
---

# Define Tech Stack Workflow

This workflow bridges the gap between MVP Ideation and System Design. It establishes the "C4 Level 1 & 2" architecture by defining the global tools and patterns required for the MVP.

**Prerequisite:** The idea has been validated (`/validate-idea`) and reduced to an MVP (`/define-mvp`). The `docs/01_Concept.md` holds the vision.

## Step 1: Requirements Analysis
Read `docs/01_Concept.md`. Understand the MVP scope. What kind of application is this? (e.g., A real-time multiplayer game requires different tech than a static blog).

## Step 2: Architecture Proposal
Determine the most pragmatic and efficient Engine/Framework, Language, Database, and State Management solution to build the MVP quickly. Follow the "Keep It Simple, Stupid" (KISS) principle.

## Step 3: Populate 02_TechStack.md
Update the `docs/02_TechStack.md` file with the finalized technologies. Add actual links to the documentation of the chosen libraries so future agents have easy access.

## Step 4: Populate Global Architecture
Update `docs/01_Concept.md` specifically under the `## Fundamental Design Decisions` section. Lock in the global architecture pattern (e.g., "We will use an Event-Driven Architecture with an SSOT pattern") based on the tech stack chosen.

## Step 5: The System Roadmap (Architektur-Schnitt)
Direkt im Abschluss des Tech-Stacks passiert die wichtigste "Translation": Zerschneide die MVP-Features aus `01_Concept.md` in abstrakte C4-Systemblöcke (z.B. 1. Database, 2. Auth, 3. TradingEngine). 
- Erstelle dazu die Datei `docs/systems/_System_Roadmap.md` und liste diese abstrahierten Kern-Systeme auf. Setze leere Checkboxen `[ ]` davor.

## Step 6: The Handoff
Navigiere den User zum nächsten Schritt:
> *"Das Fundament und die System-Roadmap stehen. Gibt es noch tiefergehendes Fachwissen, das ich aus PDFs extrahieren soll (`/ingest-knowledge`), oder sollen wir die Codebase direkt generieren (`/init-codebase`)?"*