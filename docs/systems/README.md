# Systems Index & Design Standards

Willkommen im `docs/systems/` Verzeichnis. Hier wird jedes funktionale System (z.B. DataStore, NPCs, Kamera) einzeln dokumentiert.

## System Index
*(Wird von Agenten automatisch gepflegt)*

- [Leerer Index - Füge hier Systeme hinzu]

## Design Standards (IMPORTANT FOR AGENTS)
Wenn du ein neues `<System_Name>.md` anlegst, MUSST du strikt folgende C4 Level 3 Struktur einhalten:

1. **Component Overview:** Kurze Zusammenfassung im C4 Kontext.
2. **Architecture Diagram (Mermaid):** Flowchart/Class-Diagramm (ACHTUNG: Keine Sonderzeichen in Knoten!).
3. **Public Interfaces (API):** Welche Methoden/Events stellt das System für *andere* Systeme zur Verfügung?
4. **Dependencies:** Welche anderen Systeme werden aufgerufen?
5. **Data Structures:** Kerndatenstrukturen (z.B. State Atoms).
6. **Known Limitations / Edge Cases:** Aktuelle Einschränkungen.
7. **Testing & Verification:** Wie testet man das System (Unit Tests, UI Flows etc.)?
