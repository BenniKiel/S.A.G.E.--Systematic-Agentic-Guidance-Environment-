---
description: Führt einen ressourcenschonenden "Surface Scan" über rohe Wissensquellen aus, um Architektur-Empfehlungen (Blueprint) vor einem MVP zu extrahieren.
---

# 🏗️ Workflow: /blueprint-domain
Dieser Workflow wird genutzt, wenn der Nutzer sich in einer fremden Nische oder Domäne bewegt (z.B. "Quant Trading") und noch kein existierendes MVP (`01_Concept.md`) definiert hat. Anstatt ganze Fachbücher iterativ und teuer zu lesen, erstellt dieser Befehl über einen schnellen, token-sparenden Surface-Scan eine rohe Architektur-Strategie, die als R&D Vorlage für das MVP dient.

## 0️⃣ Schritt 0: Format Pre-Check
- Prüfe, ob die vom Nutzer genannten Ziel-Quellen als `.pdf` in `.agents/knowledge/_raw/` vorliegen.
- Wenn ja: Führe ZWINGEND in der Kommandozeile (`run_command`) das S.A.G.E. Tool `.agents/scripts/pdf_to_md.py [pdf_file.pdf]` aus.
- Arbeite danach AUSSCHLIEßLICH mit der generierten `.md` Rohtext-Datei weiter.

## 1️⃣ Schritt 1: Surface Scan (Die Makro-Suche)
- **WICHTIG:** Vermeide zwingend Deep Reads oder iteratives Chunking des gesamten Buches! Das würde Token-Limits sprengen.
- Führe gezielte Scanner-Arbeiten auf dem Rohtext aus:
  1. Lies die obersten Zeilen / das Inhaltsverzeichnis (TOC) der Markdown-Datei (z.B. limitierter Zeilenaufruf `view_file` auf Zeile 1-500).
  2. Nutze zwingend `grep_search` im Terminal nach Schlüsselbegriffen wie "System", "Architecture", "Components", "Data", "Microservices", "Database", "API".
  3. Lies nur die unmittelbaren Abschnitte rund um diese Suchtreffer, um die Kernphilosophie und Architektur-Ratschläge des Autors zu extrahieren.

## 2️⃣ Schritt 2: The Domain Blueprint
- Kondensiere das abgeleitete Architektur-Wissen in exakt EIN Dokument: **`docs/research/Domain_Blueprint.md`** (lege den Ordner falls nötig an).
- Das Dokument MUSS folgende Struktur haben:
  1. **Die Kern-Philosophie:** (Knappe Zusammenfassung der Paradigmen der Autoren).
  2. **Architektur (Baseline & Overlay):** Liste die absoluten Standard-Grundsysteme auf (dein eigenes generisches LLM-Wissen: z.B. DB, App-Server) und kennzeichne die hochspezialisierten Experten-Zusätze aus der Quelle explizit als "(Overlay)". Das verhindert das "Fundamental-Vakuum".
  3. **Konfliktlösung (Pfade):** Gibt es Widersprüche zur KISS-Philosophie von S.A.G.E.? Definiere "Option A" (z.B. Monolith, simpel) und "Option B" (z.B. Microservices, komplex) und sprich zwingend eine präferierte Empfehlung für das zu bauende MVP aus.
  4. **Extraction Map:** Gehe das gelesene Inhaltsverzeichnis (TOC) durch. Notiere explizit, *welche Kapitel* später für tiefes Coding-Wissen nützlich sind und welche ignoriert werden können (z.B. "Kapitel 1-4 = Historie (ignorieren). Kapitel 5-8 = Mathematik (relevant).").

## 3️⃣ Schritt 3: The Handoff
- Speichere das `Domain_Blueprint.md` final ab.
- Informiere den User prägnant im Chat über die ermittelten Optionen und den Surface Scan.
- **Handlungsaufforderung (Handoff):** Navigiere den User zwingend in den "Choke Point" des Tunnels:
  > *"Der Blueprint steht! Da wir nun wissen, WIE die Profis das bauen, lass uns unser Projekt jetzt zwingend greifbar machen und das MVP schnüren (`/define-mvp`)."*
