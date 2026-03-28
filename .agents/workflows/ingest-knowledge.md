---
description: Inhalts-Extraktion & Format-Konvertierung riesiger Quellen in atomares Projekt-Wissen (HDKI).
---

# 📚 Workflow: /ingest-knowledge
Dieser Workflow befähigt S.A.G.E., riesige PDF-Bücher, wissenschaftliche Papers oder Docs iterativ zu "lernen", ohne das LLM Context-Window in die Knie zu zwingen und "Lost-in-the-Middle" Phänomene auszulösen.

## 0️⃣ Schritt 0: Format Pre-Check (PDF Parsing)
- Prüfe, ob die vom Nutzer genannten Ziel-Quellen als `.pdf` vorliegen (zumeist in `.agents/knowledge/_raw/`, falls vom User angelegt).
- Wenn ja: Führe ZWINGEND in der Kommandozeile (`run_command`) das S.A.G.E. Tool `.agents/scripts/pdf_to_md.py [pdffile.pdf]` aus.
- Ignoriere das ursprüngliche PDF von nun an. Arbeite in den Folgeschritten AUSSCHLIEßLICH mit der vom Tool generierten `.md`-Datei als Quelle.

## 1️⃣ Schritt 1: The Pre-Flight Check (Source Profiling)
- Lese mit begrenzten Limits (z. B. erste 1000 Zeilen) das Inhaltsverzeichnis (TOC) der `.md` Quelle.
- **WICHTIG (Extraction Map):** Prüfe, ob `docs/research/Domain_Blueprint.md` existiert. Falls ja, richte dich HERMETISCH nach der dortigen "Extraction Map" (überspringe strikt die Kapitel, die im Blueprint als irrelevant markiert wurden!).
- Lese das Projekt-Konzept `docs/01_Concept.md`, um die "Project Lens" (Fokus des Projekts) zu verstehen.
- Ermittele anhand beider Dateien die Kernphilosophie der Quelle im Bezug auf euer eigenes Projekt.
- **Token Estimation**: Schätze die Hard-Tokens der gesamten Rohtext-Datei ab (Regel: Wörterzahl * 1.3 ≈ Tokens).
- Präsentiere dem User das "Source Profile" im Chat:
  > *"Ich habe die Quelle profiliert. Sie vertritt die Kernphilosophie [X]. Die gesamte Extraktion wird ca. [Y] Iterationen und [Z] Input Tokens kosten. Unser Projektfokus ist [W]. Welchen Paradigma-Tag soll ich vergeben (z.B. `[ActiveCrypto]`) und soll ich das Buch komplett, oder nur in bestimmten Kapiteln iterieren?"*
- **HARD STOP:** Warte zwingend auf die Antwort des Users!

## 2️⃣ Schritt 2: The Iterative Loop (Chunking)
- Beginne das referenzierte Lesen in Batches (max 3-5 Chunks am Stück, um LLM-Degradation vorzubeugen).
- Lese Chunk 1 (z. B. Kapitel 1) durch gezieltes Ansteuern von Textbereichen.
- Erstelle in `docs/knowledge/` hochverdichtete "Knowledge Items" (KIs). Jeder KI (max. ca. 150 Zeilen) deckt exakt EIN atomares Thema ab.
- **WICHTIG (Namespacing):** Prefix die generierten Dateien IMMER mit dem freigegebenen Paradigma-Tag (z.B. `KI-[Tag]-Indikatoren.md`). So vermeidest du spätere Widersprüche bei Multibuch-Analysen.

## 3️⃣ Schritt 3: Rolling Memory (Der Index)
- Nach fedem Chunk aktualisierst du zwingend `docs/knowledge/_Knowledge_Index.md`.
- Vermeide Index-Bloating! Im Index stehen ausschließlich:
  1. Ein ultra-kurzes Glossar elementarer Begriffe (max. 50 Zeilen Hard-Limit).
  2. Indexierte Links zu den `KI-*.md` Dateien, streng gruppiert unter ihrem `[Tag]`.
- **WICHTIG (Rolling Memory):** Bevor du in Iteration X+1 einen weiteren Chunk liest, öffnest du zur Gedächtnisauffrischung kurz deinen eigens generierten `_Knowledge_Index.md`!

## 4️⃣ Schritt 4: Batch-Check & The Handoff
- Nach einem Batch verlangst du via Chat die Bestätigung vom User ("Type 'Go' für Kapitel X").
- **Am Ende (The Handoff):** Wenn alle relevanten Chunks verarbeitet wurden, moderiere den Übergang in die Code-Phase:
  > *"Spezialwissen ist gelernt und als atomare KIs indexiert. Lass uns nun die Codebase initialisieren (`/init-codebase`)."*
