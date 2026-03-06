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
│       ├── setup-workspace.md
│       ├── validate-idea.md
│       ├── define-mvp.md
│       ├── define-techstack.md
│       ├── create-system.md
│       └── record-decision.md
└── README.md
```

---

## 🚀 Quickstart: The "Zero-to-One" Pipeline

To start a new project with S.A.G.E., clone this repository, open an Agent-enabled IDE (like Antigravity / Cursor / Copilot Workspace), and follow this exact sequence:

### 1️⃣ Phase 0: The Empty Canvas
Open an Agent Chat and prompt: 
> *"Execute the `/setup-workspace` workflow."*

*(The Agent will scaffold your `docs/` folder, laying out empty `01_Concept.md`, `02_TechStack.md`, and the `systems/` index).*

### 2️⃣ Phase 1: Ideation & MVP (No Code Allowed)
Prompt: 
> *"I have an idea for [Your Idea]. Execute `/validate-idea`."*

*(Agent searches the web, defines target audience and USP).* <br/>
Prompt: 
> *"Let's scope this down. Execute `/define-mvp`."*

*(Agent applies MoSCoW method and locks the MVP scope into `docs/01_Concept.md`).*

### 3️⃣ Phase 2: Global Architecture
Prompt: 
> *"Execute `/define-techstack` based on our MVP."*

*(Agent defines the Engine, Database, and State Management patterns in `docs/02_TechStack.md`).*

### 4️⃣ Phase 3: Component Design
Prompt: 
> *"Execute `/create-system` for a new 'Authentication' system."*

*(Agent designs a C4 Component Diagram in `docs/systems/`, asks for permission, and HARD STOPS).*

### 5️⃣ Phase 4: Execution
Prompt: 
> *"The Authentication C4 design is approved. Implement the code."*

*(Agent finally writes code, knowing exactly what constraints exist, and automatically updates documentation afterwards).*

---

## 📖 User Guideline

For an in-depth explanation of how to talk to Agents, handle edge cases, and perform troubleshooting, please read the `docs/Workspace_Guideline.md` generated after running `/setup-workspace`.

<br/>
<div align="center">
  <i>Built for developers who want the speed of AI without sacrificing the discipline of Software Engineering.</i>
</div>
