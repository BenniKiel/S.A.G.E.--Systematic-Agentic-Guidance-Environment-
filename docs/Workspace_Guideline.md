# Agentic Workspace - User Guideline

Herzlichen Glückwunsch! Du hast nun ein robustes System aufgebaut, das deine KI-Agenten zwingt, methodisch und vorhersehbar zu arbeiten. Dieses Dokument dient dir als Referenz, wie du den Workspace in künftigen Projekten aufsetzt und deine Agenten promptest, um das Maximum herauszuholen.

## 0. Die Ordnerstruktur (Der allererste Schritt)

Wenn du ein komplett neues Projekt beginnst, musst du den Agenten erst das "Papier" geben, auf dem sie arbeiten können.

1. **Ordnerstruktur kopieren:** Kopiere den gesamten `.agents/` Ordner (inklusive `skills/` und `workflows/`) aus diesem Projekt in das Root-Verzeichnis deines neuen Projekts.
2. **Workspace initialisieren:** Öffne einen neuen Chat mit deinem Agenten (z.B. Antigravity) und schreibe einfach:
   > *"Bitte führe den `/setup-workspace` Workflow aus."*
   Der Agent legt die leere Basisstruktur (`docs/01_Concept.md`, `docs/02_TechStack.md`, etc.) an.

## 1. Die Ideation-Phase: Markt & MVP definieren (VOR dem Coden)

Oft scheitern Projekte, weil zu früh Code geschrieben wird. Dein Agentic Workspace hat zwei mächtige "Product Manager" Workflows eingebaut, die du nutzen solltest, *bevor* du an Architektur denkst.

1. **Idee validieren:** Öffne einen Chat und schreibe: 
   > *"Ich habe eine Idee für ein neues Projekt: [z.B. Tinder für Hunde]. Bitte führe den `/validate-idea` Workflow aus."*
   Der Agent füllt das leere `01_Concept.md` mit Zielgruppen und USP-Daten.

2. **Den MVP festzurren:** Wenn die Idee gut ist, schreibe:
   > *"Lass uns den Scope eingrenzen. Bitte führe den `/define-mvp` Workflow aus."*
   Der Agent streicht alle "Nice-to-haves" aus `01_Concept.md` und definiert dein Minimum Viable Product.

## 2. Der perfekte Start: Die Global Architecture festlegen

Bevor ein Agent ein Einzelsystem (Auth, Payment) designt, muss der globale Tech-Stack (C4-Level 1 & 2) stehen.

**Optimaler Start-Prompt:**
> *"Unser Konzept steht in `01_Concept.md`. Bitte führe den `/define-techstack` Workflow aus, um die passenden Frameworks und die grobe Architektur für diesen MVP festzunageln."*

Der Agent wird `02_TechStack.md` ausfüllen und Architektur-Patterns (wie MVC oder Event-Driven) empfehlen.

**Warum dieser Prompt funktioniert:**
- Er verweist explizit auf die Skills (damit der Agent den Kontext lädt).
- Er triggert den `structured_problem_solving` Skill (Zwingt den Agenten zum Stoppen und Nachfragen).

## 3. Codebase Initialisierung (Das Fundament gießen)

Wenn der Tech-Stack beschlossen ist, brauchst du erst einmal das leere Projektgerüst in deinem Ordner, bevor du einzelne Systeme erstellst.

**Optimaler Prompt:**
> *"Unser Tech-Stack steht. Bitte führe den `/init-codebase` Workflow aus, um das grundlegende Projektgerüst (Framework etc.) in diesem Ordner zu installieren und aufzusetzen."*

Der Agent liest den Tech-Stack und führt die nötigen CLI-Commands aus (z.B. `npx create-next-app`, `npm init` etc.), um das leere Projekt bereitzustellen.

## 4. Wie man Agenten im Alltag "richtig" promptet

Dank deiner neuen Skills musst du Agenten nicht mehr mikromanagen ("Erstelle ein File hier, aktualisiere die Doku da, mach langsam..."). Die Skills übernehmen das.

### A. System Design anfragen (C4 Level 3)
Sobald Codebase, Tech Stack und Konzept stehen, konzipierst du Systeme einzeln:
> *"Ich brauche ein neues Authentication-System. Bitte führe den `/create-system` Workflow für ein 'Auth_System' aus."*

*Was im Hintergrund passiert:* Der Agent liest die Docs, erstellt das C4-System-Dokument in `docs/systems/` inkl. Diagramm, stoppt und bittet um Erlaubnis. **Er schreibt in diesem Workflow keinen Code!**

### B. Die Implementierung starten (Coding)
Wenn du das System-Design (A) abgenickt hast, gibst du den Startschuss für echten Code:
> *"Das Auth-Design sieht super aus. Setze es nun im Code um."*

### B. Bestehenden Code anpassen / Bugs fixen
Du musst dir keine Sorgen mehr machen, dass die Doku veraltet. Ein einfacher Prompt reicht, der Skill `continuous_documentation` greift automatisch:
> *"Füge dem bestehenden Auth_System eine Funktion hinzu, mit der User ihr Passwort zurücksetzen können."*

*Was im Hintergrund passiert:* Der Agent liest (hoffentlich) automatisch `docs/systems/Auth_System.md`, schreibt den Code und aktualisiert danach ungefragt das Markdown-Dokument, um die neue API/State-Logik abzubilden.

### C. Wichtige Entscheidungen festhalten (ADRs)
Oft entstehen in Chats wichtige "Warum?"-Entscheidungen (z.B. "Gut, dann nutzen wir PostgreSQL statt MongoDB."). Um dieses Wissen zu speichern, nutze den neuen Workflow:
> *"Wir haben uns gerade für PostgreSQL entschieden. Bitte dokumentiere das über den `/record-decision` Workflow."*

*Was im Hintergrund passiert:* Der Agent legt automatisch ein neues MADR Dokument fortlaufend nummeriert (z.B. `docs/decisions/0002-use-postgresql.md`) an und dokumentiert den Kontext dieser Entscheidung für alle zukünftigen Agenten.

## 4. Troubleshooting & Best Practices

1. **Agenten vergessen Mermaid Diagramme:** Der `system_design_standards` Skill verlangt zwingend Mermaid-Diagramme für die C4-Komponenten in `docs/systems/`. Zeigt der Agent sich faul, weise ihn zurecht: *"Du hast im C4-Component-Dokument das Mermaid-Diagramm vergessen. Hol das nach!"*
2. **Agenten "vergessen" die Regeln:** Manchmal laden Agenten ihren Kontext nicht tief genug. Wenn ein Agent voreilig Code schreibt oder die Doku vergisst, erinnere ihn streng an seine Skills: 
   > *"Stopp. Hast du den `structured_problem_solving` Skill ignoriert? Lösche den Code, lies die Docs und mach einen Entwurf."*
3. **Zu große Systeme:** Wenn ein System-Dokument (eine C4 Component) in `docs/systems/` extrem lang wird (z.B. >300 Zeilen), weise den Agenten an, das System in Sub-Komponenten (z.B. `Auth_OAuth.md`, `Auth_JWT.md`) aufzuspalten und die Diagramme in der `README.md` zu aktualisieren.
4. **Tech Stack aktuell halten:** Wenn du selbst neue Frameworks installierst oder neue Paradigmen einführst, trage sie händisch in `docs/02_TechStack.md` ein. So wissen alle künftigen Agenten sofort Bescheid.

---
**Zusammenfassung:** Die Magie dieses Setups liegt im Vertrauen auf die formale Skill-Struktur. Prompte deine Absicht (das "Was"), die Agenten kümmern sich durch ihre Skills und Workflows um den Prozess (das "Wie").
