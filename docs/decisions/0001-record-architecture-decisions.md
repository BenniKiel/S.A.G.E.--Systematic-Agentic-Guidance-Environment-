# Record Architecture Decisions

*Status: accepted*
*Date: 2026-03-06*

## Context and Problem Statement
In komplexen Agentic Coding Projekten treffen AI-Agenten (und der User) hunderte kleine und große Architekturentscheidungen (welche Library, welches Design Pattern, welche State-Management-Variante). 
Ohne historische Aufzeichnungen geht der Kontext für diese Entscheidungen nach wenigen Wochen verloren. Künftige Agenten oder neue Teammitglieder verstehen nicht mehr, *warum* das System so designt wurde, wie es ist.

## Decision Drivers
* Bedarf an einem Langzeitgedächtnis für das Projekt.
* Die Notwendigkeit, schnell auf den Kontext früherer Entscheidungen zugreifen zu können, ohne lange Chat-Historien zu durchsuchen.
* Agenten benötigen klare, einheitliche Templates.

## Considered Options
* Dokumentation von Entscheidungen innerhalb der Code-Kommentare.
* Ein einzelnes, riesiges `Decisions.md` Dokument.
* Architecture Decision Records (ADRs) im Markdown (MADR) Format in einem dedizierten `docs/decisions/` Ordner.

## Decision Outcome
Wir haben uns für den Einsatz von **Architecture Decision Records (ADRs)** im MADR-Format entschieden. 

Diese Methode zwingt Agenten durch den `architecture_decision_records`-Skill, Architekturentscheidungen isoliert, chronologisch und kontextreich zu dokumentieren. Jeder Agent kann künftig via Workflow den Befehl `/record-decision` nutzen, um ein neues MADR anzulegen.

### Positive Consequences
* Ein persistentes, maschinenlesbares Architektur-Gedächtnis entsteht.
* Agenten können frühere Fehlentscheidungen reproduzieren und verstehen.
* Das C4-Komponenten-Design wird durch klare Design-Historie untermauert.

### Negative Consequences
* Geringfügiger Overhead bei der Projektarbeit, da Agenten angewiesen werden müssen, ADRs zu schreiben (was durch Workflows minimiert wird).
* Der `docs/decisions/` Ordner kann bei fehlender Pflege unübersichtlich werden.
