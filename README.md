<div align="center">
  <h1>🧠 S.A.G.E.<br/><sub>Systematic Agentic Guidance Environment</sub></h1>
  <p><strong>A framework that turns chaotic AI coding agents into disciplined Lead Architects.</strong></p>

  <p>
    <a href="#-the-problem"><img alt="Status" src="https://img.shields.io/badge/Status-Production%20Ready-success?style=for-the-badge&logoColor=white" /></a>
    <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge&logoColor=white" /></a>
  </p>
</div>

<br/>

## 🚨 The AI Coding Problem
Working with AI coding agents typically leads to 3 massive failures in mid-to-large projects:

1. ❌ **"Feature Creep"**: Building complex systems without validating the market need or scoping an MVP first.
2. ❌ **"The Blind Architect"**: Agents writing 2,000 lines of spaghetti code without agreeing on a global Tech Stack or State Management pattern beforehand.
3. ❌ **"Context Window Death"**: Projects collapse when agents try to read 50 obsolete markdown files at once, causing massive token flooding and hallucinations.

---

## ✨ The S.A.G.E. Solution

S.A.G.E. is a powerful, uncompromising **"Zero-to-One"** pipeline. Instead of letting agents hallucinate entire codebases based on a single prompt, S.A.G.E. forces them to follow a military-grade development pipeline: 

<div align="center">
  <b>Market Validation ➡️ MVP Scoping ➡️ C4 Architecture Design ➡️ ADR Documentation ➡️ Execution.</b>
</div>

<br/>

### 🎯 Key Features
| Feature | How it works |
| :--- | :--- |
| **Product Management** | Workflows to validate raw ideas (`/validate-idea`) and ruthlessly strip away non-essential features (`/define-mvp`) *before* architecture starts. |
| **Knowledge Integration** | Erlaubt Agenten über `/ingest-knowledge` massive PDFs per "Iterative Chunking" in kleine, verdauliche Markdown-Konzeptbausteine (KIs) zu zerlegen, ohne den Token-Context zu sprengen. |
| **Enforced C4 Design** | Agents must design a C4 Component Level document (incl. Mermaid.js diagrams) and receive *User Approval* before writing any code. |
| **Automated ADRs** | A streamlined `/record-decision` workflow ensures "Why did we choose this Database?" decisions are logged using the MADR standard. |
| **Token Optimization** | Agents are forced to use `grep` searches instead of full document reading to save tokens and prevent context flooding. |

---

## �️ The Workspace Anatomy

When you clone S.A.G.E. into your project, you get an `.agents/` brain that orchestrates everything behind the scenes:

```text
SAGE-Workspace/
├── .agents/                    # The S.A.G.E. Engine (Do not delete)
│   ├── skills/                 # The strict rulesets the Agent MUST follow
│   │   ├── architecture_decision_records/  # Enforces MADR
│   │   ├── continuous_documentation/       # Enforces grep-search & Orphan Prevention
│   │   ├── structured_problem_solving/     # 4-Phase Iterative Design Loop
│   │   └── system_design_standards/        # Enforces C4 Level 3 & Testing Standards
│   └── workflows/              # The Slash-Commands the user triggers
│       ├── begin-project.md
│       ├── setup-workspace.md
│       ├── validate-idea.md
│       ├── blueprint-domain.md
│       ├── define-mvp.md
│       ├── define-techstack.md
│       ├── ingest-knowledge.md
│       ├── create-system.md
│       ├── record-decision.md
│       └── wrap-mvp.md
└── README.md
```

---

## 🚀 Quickstart: The "Zero-to-One" Pipeline

To start a new project with S.A.G.E., clone this repository, open an Agent-enabled IDE (like Antigravity / Cursor / Copilot Workspace), and follow this exact sequence:

### 1️⃣ Phase 0: The Empty Canvas
Open an Agent Chat and prompt: 
> *"Execute the `/begin-project` workflow."*

*(The Agent will act as a Project Manager, scaffold your `docs/` folder via `/setup-workspace`, and guide you interactively through the entire S.A.G.E. funnel).*

### 2️⃣ Phase 1: Ideation & MVP (No Code Allowed)

**Weg A (Der Standard-Weg):** Du hast die pure Idee im Kopf.
Prompt: 
> *"I have an idea for [Your Idea]. Execute `/validate-idea`."*

*(Agent searches the web, defines target audience and USP).* <br/>
Prompt: 
> *"Let's scope this down. Execute `/define-mvp`."*

**Weg B (Der "Knowledge-First" Weg für Nischen):** Du hast keine Ahnung von der Architektur, aber tolle PDFs.
Lege die Dokumente in `.agents/knowledge/_raw/`.
Prompt:
> *"Execute `/blueprint-domain` auf meinen Dokumenten."*

*(Agent zieht die Branchen-Standards und Architektur-Optionen als Blueprint heraus).*  <br/>
Prompt:
> *"Execute `/define-mvp` basierend auf dem Blueprint."*

*(Agent konstruiert logisch das MVP und speichert es in `docs/01_Concept.md`).*

### 3️⃣ Phase 2: Global Architecture
Prompt: 
> *"Execute `/define-techstack` based on our MVP."*

*(Agent defines the Engine, Database, and State Management patterns in `docs/02_TechStack.md`).*

### 4️⃣ Phase 3: R&D / Knowledge Gathering (Optional)
Prompt:
> *"Execute `/ingest-knowledge` to read the complex setup guide in the `_raw` folder."*

*(Agent parses PDF via Python, performs a Source Profile pre-flight check, and iteratively generates isolated Markdown Knowledge Items (KIs) into `docs/knowledge/`).*

### 5️⃣ Phase 4: Project Initialization
Prompt: 
> *"Execute `/init-codebase` to scaffold the framework based on our tech stack."*

*(Agent runs CLI commands like `npx create-next-app` or sets up the physical folder structure for the engine).*

### 6️⃣ Phase 5: Component Design
Prompt: 
> *"Execute `/create-system` for a new 'Authentication' system."*

*(Agent reads the Knowledge Index, designs a C4 Component Diagram in `docs/systems/`, asks for permission, and HARD STOPS).*

### 7️⃣ Phase 6: Execution (The Build Loop)
Prompt: 
> *"The Authentication C4 design is approved. Implement the code."*

*(Agent writes the code. Afterwards, they enforce a QA-Gate and ask you to test it locally. Once verified, they check Auth off the `_System_Roadmap.md` and move to the next system).*

### 8️⃣ Phase 7: The Launch
Prompt:
> *"All systems are checked off! Execute `/wrap-mvp`."*

*(Agent runs a final QA check against the MVP Concept, writes a clean project README, and concludes Version 1.0).*

---

## 📖 User Guideline

For an in-depth explanation of how to talk to Agents, handle edge cases, and perform troubleshooting, please read the `docs/Workspace_Guideline.md` generated after running `/setup-workspace`.

<br/>
<div align="center">
  <i>Built for developers who want the speed of AI without sacrificing the discipline of Software Engineering.</i>
</div>
