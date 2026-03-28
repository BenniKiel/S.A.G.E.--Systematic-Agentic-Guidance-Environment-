# Concept: High-Density Knowledge Integration (HDKI)

## 1. Problemstellung
Nischenprojekte und hochspezialisierte Domänen erfordern tiefes Fachwissen, das LLMs standardmäßig nicht besitzen. Ein simples "Kopieren von PDFs in den Chat" schöpft das Context-Window aus, erhöht die Token-Kosten massiv, verringert die "Attention" für kritische Details und verwässert den Fokus des Agenten beim Programmieren.

## 2. Antworten auf die Kernfragen

### 2.1 Generelle vs. Projektspezifische Informationen
- **Projektspezifisch**: Der Fokus dieses Features. Spezifisches Domain-Wissen (z. B. Fachbücher, wissenschaftliche Papers, proprietäre API-Dokumentationen) wird direkt im lokalen Repository unter `.agents/knowledge/` hinterlegt. Das hält das Wissen isoliert pro Projekt.
- **Generell**: Übergeordnetes Wissen (Patterns, Architektur, Coding-Richtlinien) wird weiterhin über die globalen `skills/` abgedeckt. Extrahiertes Domain-Wissen könnte jedoch bei breiter Anwendbarkeit teilweise in Skills überführt werden.

### 2.2 Format für minimale Input-Token & einfache Auffindbarkeit
- **Format**: Atomic Markdown Notes (inspiriert vom *Zettelkasten*-Prinzip).
- Komplexe Texte aus Quellen werden durch den Agenten in kleine, hochdichte Markdown-Dateien kondensiert (KIs - Knowledge Items). Jeder KI behandelt exakt ein atomares Konzept (z. B. `KI-Ablauf_Authentifizierung.md`).
- **Auffindbarkeit**: Es gibt einen zentralen `_Knowledge_Index.md`. Der Agent sucht zuerst in diesem Index und lädt dann über zielgerichtetes Lesen (`view_file` oder automatischen IDE-Einbezug) nur die 1–3 relevanten `KI-*.md` Dateien in seinen Kontext, statt das ganze Quellmaterial zu parsen.

### 2.3 API vs. IDE integrierte LLMs
- **IDE integrierte LLMs**: Dies ist der empfohlene Weg, um die Komplexität (KISS-Prinzip) gering zu halten.
- Moderne KI-IDEs (Cursor, Antigravity, Copilot) haben Workspace-Indexierung und RAG (Retrieval-Augmented Generation) native eingebaut. Liegt das Wissen formatiert und verdichtet im Workspace, steuern die internen Engines der IDE den optimalen Abruf.
- **Verzicht auf externe APIs**: Es wird keine externe Vektordatenbank oder RAG-API benötigt. Die nativen IDE-Fähigkeiten in Kombination mit einem strikten, agenten-getriebenen Workflow (`grep_search` & `view_file`) übertreffen komplexe Third-Party RAGs in der tagtäglichen Code-Entwicklung deutlich.

### 2.4 Integration in das S.A.G.E. Projekt (UX & Praktikabilität)
Um das Feature nahtlos in die bestehende S.A.G.E.-Pipeline zu integrieren, werden zwei Komponenten benötigt:

1. **Neuer Workflow: `/ingest-knowledge`**
   - **UX**: Der Entwickler legt Rohdaten (als `.txt` / `.md` Dumps von Papers/Büchern) in einen temporären Ort (z.B. `.agents/knowledge/_raw/`).
   - **Aktion**: Der Nutzer führt `/ingest-knowledge` aus.
   - **Ergebnis**: Der Agent verarbeitet die Quelle iterativ, extrahiert die Kernkonzepte, speichert sie als dichte Markdown-Dateien in `.agents/knowledge/processed/` und aktualisiert den zentralen `_Knowledge_Index.md`.

2. **Neuer Skill: `domain_knowledge_retrieval`**
   - Ein dedizierter Skill, der bei Architekturentscheidungen und Code-Generierungen instruiert: *"Durchsuche zwingend den `_Knowledge_Index.md`, bevor du bei unklaren Domain-Anforderungen Annahmen triffst."*

### 2.5 Verarbeitung von extrem großen Quellen (z.B. Bücher)
Dokumente mit hunderten Seiten (wie Trading-Bücher) überlasten das "Context Window" oder führen zu Detailverlust ("Lost in the Middle"-Problem), wenn sie in einem Rutsch konsumiert werden. Deshalb nutzt der `/ingest-knowledge` Workflow einen **iterativen Chunking-Ansatz**:
1. **Initialer Scan**: Der Agent liest zuerst nur das Inhaltsverzeichnis (bzw. die ersten 500-1000 Zeilen), um den Aufbau der Quelle zu verstehen.
2. **Segmentierung**: Er plant das Lesen in logischen Blöcken (z.B. Kapitel für Kapitel).
3. **Loop-Extraktion**: Der Agent liest durch Werkzeuge (z.B. `view_file` mit `StartLine`/`EndLine` Argumenten) gezielt **nur** Kapitel 1, generiert daraus kleine, modulare KIs, trägt diese in den `_Knowledge_Index.md` ein, und geht dann nahtlos zu Kapitel 2 über, bis alles abgearbeitet ist.
Dadurch wird absolut kein Detail vergessen und die Token-Auslastung pro Iteration bleibt extrem gering.

### 2.6 Kontext-gesteuerte Extraktion (Lens & Memory)
Wenn der Agent in Iteration 5 das Kapitel 5 liest, darf er nicht den Sinn für das Gesamtprojekt oder die Inhalte aus Kapitel 1-4 verlieren. Dies wird programmatisch im Workflow durch zwei "Anker" gelöst:
- **Die Projekt-Linse (Project Lens)**: Bevor der Ingestion-Prozess überhaupt beginnt, wird der Agent angewiesen, das `docs/01_Concept.md` des eigenen Projekts zu lesen (oder er erfragt ein "Extraction Goal" beim User). Dadurch filtert er Informationen (Bspw. bei einem Buch über Krypto-Trading: Fokus auf algorithmische Patterns, Ignorieren der Psychologie-Kapitel, falls das Projekt ein automatisierter Bot ist).
- **Das Rollierende Gedächtnis (Rolling Memory)**: Der `_Knowledge_Index.md` ist nicht nur ein Inhaltsverzeichnis, sondern enthält eine komprimierte *Global Summary* und ein *Glossar*. Vor jedem neuen Chunk liest der Agent frisch den aktuellen `_Knowledge_Index.md`. So "erinnert" er sich, welche Projektkonzepte bereits gesammelt wurden und wie Begriffe im Buch bisher definiert wurden.

### 2.7 Source Profiling & Konflikt-Management
Bei großen, teils widersprüchlichen Quellen (z.B. Trading-Buch A rät zu passivem ETF-Sparen, Buch B schwört auf aktives Daytrading) darf das extrahierte Wissen nicht als "absolute Wahrheit" vermischt werden. Um den User zu entlasten und Konflikte zu vermeiden:
1. **Der Pre-Flight Check (Source Profiling)**: Bevor das harte Chunking beginnt, liest der Agent das Inhaltsverzeichnis und ggf. die Zusammenfassung/Einleitung. Er leitet die Kern-Philosophie der Quelle ab und erstellt ein kurzes *Source Profile*.
2. **User Alignment**: Der Agent präsentiert dem User dieses Profil ("*Dieses Buch vertritt primär aktives Daytrading*") und fragt: *"Soll ich das gesamte Buch extrahieren oder nur die technischen Indikatoren isolieren?"* Der User muss das Buch nicht kennen, kann aber mit einem Klick den Fokus schärfen.
3. **Namespacing & Paradigma-Tags**: KIs werden nicht als universelle Wahrheiten gespeichert (falsch: `KI-Indizes_sind_schlecht.md`). Stattdessen nutzt der Agent im Ingestion-Prozess zwingend **Namespaces** oder **Paradigma-Tags** im Dateinamen (korrekt: `KI-[Daytrading]-Index_Schwaechen.md`). So werden widersprüchliche Strategien im `_Knowledge_Index.md` sauber und übersichtlich gekapselt.

### 2.8 Bekannte Risiken & Limitationen (Risk Management)
Kein System ist perfekt. Bei der praktischen Umsetzung dieses Konzepts müssen zwingend folgende technische Herausforderungen im Workflow abgefangen werden:
1. **PDF-Parsing / Binärformate**: Integrierte IDE-Agenten können über `view_file` meist keine binären PDFs sauber lesen. **Lösung**: Das Feature beinhaltet ein lokales Python-Skript (`.agents/scripts/pdf_to_md.py` basierend auf `PyMuPDF4LLM`), das nativ vom Agenten in "Schritt 0" des Workflows ausgeführt wird. Es wandelt Layouts, Tabellen und Texte in sauberes, Agent-lesbares Markdown (`_raw/source.md`) um.
2. **Token-Kosten & Rate Limits**: Ein 800-Seiten-Buch in 30 Chunks zu iterieren, verbrennt extrem viele Output/Input-Tokens und kann bei metered APIs teuer werden. **Lösung**: Der Pre-Flight Check errechnet neben der Iterations-Zahl eine **harte Token-Schätzung** (z.B. Dateigröße / 4 oder Wörter * 1.3), präsentiert dem Nutzer den voraussichtlichen Gesamtaufwand in Tokens und wartet auf das "Go", bevor Kosten entstehen.
3. **Index-Bloating (Context Death durch den Index)**: Wenn der Agent hunderte KIs generiert, wird der `_Knowledge_Index.md` irgendwann selbst "zu groß" für das rollierende Gedächtnis. **Lösung**: Strikte Disziplin im Index! Er darf nur Hierarchien/Links und ein hyper-kondensiertes Glossar (max. 50 Zeilen) enthalten, aber keine tiefen Zusammenfassungen.
4. **Agent "Laziness"**: Agenten weigern sich oft, 40 Iterationen vollautomatisiert durchzuführen (Context Timeout oder "Faulheit" bei der Extraktion). **Lösung**: Der Workflow arbeitet in Batches (z. B. "Analysiere 3 Chunks, frage dann den Nutzer ob es weitergehen soll").

## 3. Workflow Simulation & System-Reflexion
Spielt man den Ablauf in der Praxis durch (Idee -> MVP -> Tech Stack -> Wissenslücke -> `/ingest-knowledge` -> `/create-system`), offenbaren sich im ursprünglichen Entwurf drei logische Schwächen, die behoben werden müssen:

### Schwäche A: Verstecktes Wissen (Ordner-Struktur)
*Problem*: Im ersten Entwurf wurden die extrahierten Markdown-Dateien in `.agents/knowledge/` abgelegt. Laut der S.A.G.E. README ist `.agents/` aber das "Do Not Touch"-Gehirn des Systems. Die kondensierten KIs sind aber exzellente Dokumentationen, die der Entwickler oft auch selbst lesen will.
*Anpassung*: Der Ausgabe-Ordner wird von `.agents/knowledge/` nach `docs/knowledge/` verschoben. Nur das rohe Arbeitsmaterial und die Skripte verbleiben versteckt.

### Schwäche B: Skill Overlapping (Bot-Psychologie)
*Problem*: S.A.G.E. hat bereits starke Skills (wie `structured_problem_solving` und `continuous_documentation`), die dem Agenten sehr strikt vorschreiben, was er vor dem Coden zu tun hat. Wenn wir nun einen isolierten `domain_knowledge` Skill hinzufügen, riskieren wir, dass der Agent im Context-Fenster entscheiden muss, welchem Skill er Priorität gibt.
*Anpassung*: Statt einen komplett neuen Skill zu schreiben, patchen wir den bestehenden Haupt-Skill (`structured_problem_solving`). Dort gibt es bereits die "Phase 1: Analysis". Dieser Phase wird die harte Regel hinzugefügt: *"If the `docs/knowledge/_Knowledge_Index.md` exists, you MUST read it to gather domain context before starting the Concept Phase."*

### Schwäche C: Die Multi-File Ingestion Falle
*Problem*: Will ein Trader 15 verschiedene Blogartikel-Texte einlesen, müsste er 15x `/ingest-knowledge Artikel_X.txt` tippen. Das ist miserable UX.
*Anpassung*: Der `ingest-knowledge` Workflow wird so geschrieben, dass er ohne Argument das komplette `_raw` Verzeichnis durchsucht. Liegen dort 5 Artikel, profiliert er alle 5, fasst den Gesamtaufwand zusammen und verarbeitet sie im Batch.

## 4. Fazit
Durch dieses System behält S.A.G.E. seine Leichtgewichtigkeit...
