# Concept: The S.A.G.E. Project Wizard (/begin-project)

## 1. Vision & UX-Zielsetzung
Das S.A.G.E. Framework bietet mittlerweile ein gewaltiges Arsenal an hochspezialisierten Workflows (`/validate-idea`, `/blueprint-domain`, `/define-mvp`, `/ingest-knowledge`). Für einen neuen Nutzer (oder selbst für Veteranen) kann es mühsam sein, den exakten Ablaufplan im Kopf zu behalten.
Die Lösung ist der **"Guided Project Wizard"**. Der Nutzer startet das Projekt mit einem einzigen Kommando: `/begin-project`. Der Agent wechselt in die Rolle eines proaktiven Senior Project Managers. Er nimmt den Nutzer visuell und textlich "an die Hand", feiert Zwischenerfolge ab und moderiert an jeder Abzweigung, wo die Reise als Nächstes hingehen kann.

## 2. Der S.A.G.E. Decision Tree (Routenplanung)
Um den Nutzer navigieren zu können, muss der Agent die logischen Phasen des S.A.G.E.-Systems verinnerlicht haben. Hier ist das Dialog-Konzept für den perfekten Onboarding-Ablauf:

### Node 0: Der Start
- **User-Input:** `/begin-project`
- **Agent-Aktion:** Begrüßt den User enthusiastisch. Erklärt in 2 Sätzen den "Zero-to-One" Ansatz von S.A.G.E. (Disziplin vor Code). 
- **Call-to-Action (CTA):** *"Zuerst müssen wir zwingend deine Workspace-Ordner anlegen. Möchtest du, dass ich `docs/` und `.agents/` jetzt über den `/setup-workspace` Befehl initiiere?"*

### Node 1: Der Ideation & Architecture Trichter (Die 3-Schritt-Reihenfolge)
Nachdem `/setup-workspace` ausgeführt wurde, leitet der Agent den Nutzer in einen flexiblen 3-Schritt-Trichter. **Das verbindliche Endziel ist zwingend Schritt 3 (Das MVP)**, aber der Nutzer kann bei Schritt 1, 2 oder direkt bei 3 einsteigen:

1. **Schritt 1: `/validate-idea` (Die rohe Idee)**
   - *Einstieg:* Der User hat nur eine grobe Vision im Kopf und startet hier als "Visionary".
   - *Handoff danach:* Der Agent fragt: *"Die Idee ist validiert! Hast du nun dicke Fach-PDFs, um daraus Architektur-Standards zu extrahieren (`/blueprint-domain`), oder weißt du eh schon genug und wir bauen direkt das MVP (`/define-mvp`)?"*
2. **Schritt 2: `/blueprint-domain` (Das Experten-Wissen)**
   - *Einstieg:* Der User startet hier direkt als "Researcher", oder er folgt der Handoff-Frage aus Schritt 1.
   - *Handoff danach:* Der Agent sagt: *"Der Blueprint steht! Da wir nun wissen, WIE die Profis das bauen, lass uns unser Projekt jetzt zwingend greifbar machen und das MVP schnüren (`/define-mvp`)."*
3. **Schritt 3: `/define-mvp` (The Mandatory Goal)**
   - *Einstieg:* Der User überspringt Schritt 1 & 2 als "Executor" ("Ich weiß exakt, was ich will"). Oder er ist der logischen Kette aus dem Blueprint/Validate gefolgt.
   - Dies ist der absolute "Choke Point" von S.A.G.E. An diesem Knoten läuft alles zusammen. Ohne ein definiertes `01_Concept.md` geht das Projekt nicht in die Phase 2 über.

### Node 2: The Tech Stack
Nachdem in Node 1 das `01_Concept.md` (MVP) fertiggestellt wurde.
- **Agent-Aktion:** *"Exzellent! Das MVP-Konzept steht. Jetzt brauchen wir Werkzeuge, um es zu bauen."*
  - **Option A:** *"Soll ich dir basierend auf den MVP-Anforderungen einen passenden, leichten Tech-Stack vorschlagen (`/define-techstack`)?"*
  - **Option B:** *"Oder hast du feste Vorgaben (z.B. Python/React)? Nenne sie mir, dann schreibe ich das `02_TechStack.md` für dich."*

### Node 2.5: The System Roadmap (Der Architektur-Schnitt)
Direkt im Abschluss des Tech-Stacks passiert die wichtigste "Translation": Die MVP-Features werden vom Agenten in C4-Modulblöcke zerlegt.
- **Agent-Aktion:** *"Das Fundament steht. Damit wir uns beim Coden nicht verrennen, habe ich dein MVP direkt in logische, entkoppelte Systeme geschnitten. Ich erstelle die Datei `docs/systems/_System_Roadmap.md`. Darin schlage ich vor, wir bauen die Systeme in dieser Reihenfolge: 1. `Database`, 2. `Auth`, 3. `TradingEngine`. Passt das für dich oder fehlt ein abstrakter Modul-Block?"*
Das zwingt das Projekt frühstmöglich in eine saubere C4-Architektur und verhindert Spaghetti-Pläne.

### Node 3: Deep Knowledge / R&D (Optional)
Nachdem der Tech Stack und die System-Roadmap stehen.
- **Agent-Aktion:** *"Die Architektur-Roadmap steht! Gibt es noch spezifisches Fachwissen (komplexe API-Docs, dicke Bücher zur Mathematik), das ich auswendig lernen muss, bevor wir Code generieren?"*
  - **Option A:** *"Ja, hier sind die Dokumente. Starten wir den Deep-Dive per `/ingest-knowledge`."*
  - **Option B:** *"Nein, unser LLM-Weltwissen reicht für dieses Projekt aus. Lass uns starten!"*

### Node 4: The System Build Loop & QA Gates (Der C4 Factory-Floor)
Wenn die vorbereitenden Phasen abgeschlossen sind, startet die Entwicklung. Der User muss nicht raten, was als Nächstes ansteht.
- **Agent-Aktion:** *"Wir sind startklar fürs Coding! Ich öffne unsere `docs/systems/_System_Roadmap.md`. Laut Plan ist System 1 (`Database`) an der Reihe. Sollen wir direkt mit `/create-system Database` loslegen?"*
- **Das QA-Gate (Quality Assurance):** Sobald der Code für ein C4-System steht, macht der Agent *nicht* sofort einen Haken auf der Roadmap. Er stoppt und zwingt den User zum lokalen Test: *"Die Implementierung für das System 'Database' ist abgeschlossen. Bitte starte das Projekt lokal (z.B. `npm run dev`) und verifiziere, ob es läuft. Gibt es Fehler? Paste sie hier zur Korrektur. Wenn alles reibungslos klappt, tippe 'Go'."*
- **Die Iterations-Schleife:** Erst nach bestandenem QA-Gate markiert S.A.G.E. das System als "[x] Done" auf der Roadmap und moderiert den nächsten Handoff: *"Glückwunsch, System Database ist verifiziert und live! Auf der Roadmap steht nun System 2 (Auth). Bereit?"*

### Node 5: The MVP Wrap-Up (Der Projektabschluss)
Die Bau-Schleife endet, wenn das letzte System auf der `_System_Roadmap.md` erfolgreich durch das QA-Gate gegangen ist. Ein echter Architekt lässt das Projekt hier nicht einfach wortlos auslaufen.
- **Der Agent-Trigger:** *"Fantastisch! Wir haben soeben das letzte Core-System auf unserer Roadmap abgeschlossen. Lass uns das Projekt offiziell abschließen (`/wrap-mvp`)."*
- **Der finale Abgleich (Definition of Done):** Der Agent führt im Hintergrund einen letzen Überflug durch und gleicht den Code-Status mit dem `01_Concept.md` ab. Wurde wirklich alles aus der "Must-Have" MoSCoW-Liste erfüllt?
- **Der Launch:** S.A.G.E. generiert automatisch ein professionell formatiertes `README.md` für das eigentliche Softwareprojekt (inklusive Run-Scripts, Systemüberblick und Architektur-Diagrammen) und verabschiedet sich: *"Version 1.0 (MVP) ist offiziell abgeschlossen und startklar für den Launch. Das S.A.G.E. Framework hat seinen Job erfüllt. Happy Hosting!"*

## 3. Die technische Implementierung
Wir müssen dafür nicht die LLM-Logik verbiegen, sondern bedienen uns zweier simpler Mechanismen:
1. **Neuer Workflow (`/begin-project.md`):** Dieser Workflow ist quasi das "Inception"-Skript. Es gibt dem Agenten die Projekt-Manager Persona und startet Node 0.
2. **Der "Handoff-Mechanismus":** Wir modifizieren die Enden von ALLEN bestehenden S.A.G.E. Workflows. (Bspw. in `/validate-idea` fügen wir ganz unten an: *Schritt 4: The Handoff -> Wenn du fertig bist, frage den Nutzer, ob wir seine validierte Idee nun über `/define-mvp` in ein Produkt gießen wollen!*). 
So reicht die Kette das Gesprächs-Token nahtlos weiter, ohne dass der User jemals den Faden verliert.
