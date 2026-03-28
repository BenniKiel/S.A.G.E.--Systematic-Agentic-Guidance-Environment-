---
description: Der offizielle Projektabschluss. Führt QA-Vergleiche durch, generiert Release-Notes und schließt V1.0 formal ab.
---

# 🎉 Workflow: /wrap-mvp
Wenn das letzte System aus der `_System_Roadmap.md` durch das QA-Gate gewandert ist, führt dieser Befehl das Projekt zu einem sauberen Release.

## Schritt 1: The Definition of Done (Der Abgleich)
- Lese unaufgefordert das `docs/01_Concept.md` (insbesondere den MoSCoW MVP-Bereich).
- Scanne die gebauten Kernsysteme im Workspace oder der `_System_Roadmap.md`.
- Schreibe einen kurzen, feierlichen Report, in dem du dem User bestätigst, dass alle "Must-Haves" aus dem initialen Konzept erfolgreich integriert wurden.
- Sollte es signifikante Abweichungen geben, erwähne diese als "Design-Entscheidungen, die wir während der Entwicklung getroffen haben".

## Schritt 2: Launch-README Generierung
- Ersetze die (oftmals noch generische oder leere) `README.md` des Wurzelverzeichnisses des Workspace.
- *Wichtig:* Dies ist NICHT S.A.G.E.'s Readme, sondern die Readme für die gebaute Ziel-Software!
- Sie sollte beinhalten:
  - Projektname & Pitch (aus dem MVP)
  - Tech Stack
  - Startanweisungen (z.B. `npm install`, `npm run dev`)
  - Abstrakte C4-Architekturübersicht

## Schritt 3: The Final Handoff (Verabschiedung)
- Informiere den Nutzer:
  > *"Version 1.0 (MVP) ist offiziell abgeschlossen und startklar für den Launch. Dein Repository ist sauber dokumentiert und getestet. Das S.A.G.E. Framework hat seinen Job für diesen Cycle erfüllt. Happy Hosting!"*
- End of Workflow.
