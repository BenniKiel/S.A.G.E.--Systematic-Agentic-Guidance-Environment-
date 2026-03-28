# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **Project Wizard (`/begin-project`)**: A fully guided, end-to-end interactive funnel moving users from Setup to Execution.
- **HDKI Pipeline**: Added `/ingest-knowledge` and `pdf_to_md.py` to recursively chunk and extract high-density knowledge from huge PDFs into atomic `.md` items.
- **Domain Blueprinting**: Added `/blueprint-domain` for fast macro-architecture extraction (Surface Scans) from unread domain PDFs prior to MVP definition.
- **MVP Wrap-Up**: Added `/wrap-mvp` to conclude projects via automated MoSCoW mapping and dynamic project-README generation.
- **System Roadmap**: Added automated C4 fragmentation (Node 2.5) during Tech Stack generation, creating an actionable `_System_Roadmap.md`.
- **QA Gates**: Inserted mandatory local verification gating inside the `/create-system` build loop before progressing on the Roadmap.
- **Feature Docs**: Concept documentation for `Feature_HighDensityKnowledge.md`, `Feature_Domain_Blueprinting.md`, and `Feature_Project_Wizard.md`.

### Changed
- **Pipeline Overhaul**: Refactored all existing 8 core S.A.G.E. workflows to include a sequential "Handoff" mechanism, guiding the user automatically.
- `structured_problem_solving` skill now enforces agents to read `docs/knowledge/_Knowledge_Index.md` before generating C4 systems.
- Updated `README.md` and `docs/Workspace_Guideline.md` to reflect the new sequential `/begin-project` entry funnel.

### Fixed
- Suppressed `pymupdf4llm` linter warnings in `pdf_to_md.py` to clean up IDE errors for missing global dependencies.
