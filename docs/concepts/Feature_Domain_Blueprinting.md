# Concept: Pre-MVP Domain Blueprinting

## 1. Problemstellung (Das Henne-Ei-Problem im R&D)
Die S.A.G.E. Pipeline verlangt strikt, dass ein Projekt mit der Definition eines MVPs (`docs/01_Concept.md`) beginnt. Alle späteren Ingestions (wie das `/ingest-knowledge` Feature) nutzen dieses MVP als Filter, um unwichtige Informationen aus enorm großen Dokumenten herauszufiltern.
Doch was passiert, wenn der Nutzer in einer völlig unbekannten, fachspezifischen Nische (z. B. "Ich will einen Quant Trading Bot bauen") startet und überhaupt nicht weiß, aus welchen Kernsystemen ein solches Projekt normalerweise besteht?
Wenn die Informationen darüber, *was* gebaut werden muss, erst in den hochkomplexen Wissensquellen stehen, scheitert der klassische "Concept-First" Ansatz von S.A.G.E., da ein User ein MVP skizzieren müsste, das fachlich mangelhaft ist.

## 2. Der Lösungsansatz: Knowledge-First Ideation
Um dieses Paradoxon aufzulösen, integrieren wir eine vorgeschaltete R&D-Phase ("Phase 0") durch einen neuen Workflow: `/blueprint-domain`.

### 2.1 Der `/blueprint-domain` Workflow
Anstatt rohe Quellen auf Coding-Formeln oder Detailwissen in KIs zu filtern (HDKI), scannt dieser Workflow das bereitgestellte Material mit einer Makro-Perspektive (**"Discovery Lens"**). 
- **Eingabe:** Der Nutzer nennt eine grobe Idee ("Trading Bot") und reicht Quellen (Bücher, Framework-Docs) im Ordner `.agents/knowledge/_raw` ein.
- **Verhalten:** Der Agent iteriert über das Material, extrahiert aber **kein** domänenspezifisches Detailwissen. Er sucht ausschließlich nach architektonischen Bauplänen, systemischen Prozessen ("Wie arbeiten Profis?") und Tech-Stack-Empfehlungen der Autoren.
- **Ausgabe:** Der Agent kondensiert seine strategischen Funde in ein einziges, exekutives Dokument: `docs/research/Domain_Blueprint.md`.

### 2.2 Anatomie des Domain Blueprints
Das generierte `Domain_Blueprint.md` ist keine fertige Software-Lösung, sondern destilliertes System-Consulting:
1. **Identifizierte Kernsysteme**: (z. B. *"Der Autor trennt das System zwingend in 'Data Ingestion', 'Alpha Generator', 'Risk Engine' und 'Execution Router'."*)
2. **Technologische Empfehlungen**: (z. B. *"Das Buch präferiert Python für die Signal-Analyse, rät aber zwingend zu C++ für Execution und Order-Routing."*)
3. **Komplexitäts-Warnungen**: (z. B. *"Vorsicht: High-Frequency Order-Books benötigen latenzarme Architektur, von der für Beginner abgeraten wird."*)

## 3. Nahtlose S.A.G.E. Synergie
Der USP dieses Features entfaltet sich in der Verknüpfung mit den bestehenden S.A.G.E. Befehlen:

**Der Übergang zum MVP (`/define-mvp`)**
Der bestehende `/define-mvp` Workflow erhält einen kleinen "Patch". Bevor der Agent ein MVP aus dem Chatverlauf skizziert, prüft er zwingend, ob `docs/research/Domain_Blueprint.md` existiert.
Findet er den Blueprint, entwirft er das `01_Concept.md` direkt aus den Experten-Vorgaben der Quelle: *"Basierend auf dem Trading-Buch schlage ich vor, die C++ Execution Engine im V1-MVP komplett wegzulassen. Stattdessen bauen wir ein reines Python-Backend für den Alpha Generator und loggen Signale als 'Paper-Trading'."*

## 4. Exemplarischer UX-Ablauf (Trading Bot)
1. **User:** Besitzt das PDF *Algorithmic Trading Systems* und legt es ungesehen in `_raw`.
2. **User:** Führt `/blueprint-domain Quant Trading` aus.
3. **Agent:** Parst das PDF zu Markdown, erkennt die Architektur eines institutionellen Bots und generiert `docs/research/Domain_Blueprint.md` mit den "Branchen-Standards".
4. **User:** Führt `/define-mvp` aus.
5. **Agent:** Liest automatisch das Blueprint und formuliert daraus ein professionelles, fundiertes `01_Concept.md` MVP für den Trading Bot.
6. **User:** Führt nun `/ingest-knowledge` auf der gleichen Datei aus.
7. **Agent:** Liest das *selbe* Buch erneut – aber diesmal wendet er das frisch abgesegnete MVP (`01_Concept.md`) als Linse an (Micro-Perspektive). Er überspringt irrelevante Kapitel und extrahiert nur die mathematischen Formeln für den Alpha Generator als `.md` Knowledge Items (KIs) passgenau in `docs/knowledge/`.

## 5. Kritische Reflexion & Skalierung (Viele große Quellen)
Betrachtet man das Konzept unter der harten Prämisse, dass ein User nicht nur ein Buch, sondern **15 dicke Fachbücher und 30 Papers** in den `_raw` Ordner wirft, offenbaren sich drei massive Schwachstellen, die den `/blueprint-domain` Workflow andernfalls lahmlegen würden:

### Schwäche 1: Der Token-Kollaps ("The Deep Read Trap")
*Problem:* Wenn der Agent alle 15 Bücher iterativ komplett durchliest (Deep Chunking), nur um grobe Architekturen für ein Blueprint zu finden, sprengt er alle API-Limits und generiert immense Kosten, bevor das Projekt überhaupt gestartet ist.
*Lösung (Surface Scan):* Der `/blueprint-domain` Befehl darf **niemals** ein iteratives Chunking des gesamten Textes ausführen. Er operiert ausschließlich im "Surface Scan"-Modus: Er liest die Inhaltsverzeichnisse (TOCs) und führt gezielte Datenbanksuchen (via Terminal `grep_search` nach systemischen Keywords wie "Architecture", "System", "Datenbank", "Microservice") durch. Er extrahiert nur die Treffer-Absätze. Das reduziert die Kosten um gut 95% und liefert die Makro-Strategie in Sekunden statt Stunden.

### Schwäche 2: Das R&D Echo ("Double Ingestion")
*Problem:* Der Agent liest das Buch für das Blueprint. Später beim `/ingest-knowledge` liest er das ganze Buch noch einmal, um die fachlichen Details zu finden. Das fühlt sich nach ineffizienter Doppelarbeit an.
*Lösung (Extraction Map):* Während des `/blueprint-domain` Surface Scans erstellt der Agent im `Domain_Blueprint.md` eine sogenannte "Extraction Map". Er listet auf: *"Ich sehe anhand der TOCs, dass Buch A in Kapitel 4-8 Indikatoren hat. Buch B Kapitel 1-5 ist reine Trading-Philosophie ohne Code-Relevanz."* Wenn später das detaillierte `/ingest-knowledge` angeworfen wird, nutzt der Agent diese Map als Navigationskarte und überspringt irrelevante Kapitel automatisch!

### Schwäche 3: Makro-Widersprüche (Architektur-Kriege)
*Problem:* Buch A propagiert eine monolithische C++ Architektur, Buch B rät zwingend zu verteilten Node.js-Microservices. Ein blindes Zusammenziehen im Blueprint führt zu einem Frankenstein-Konstrukt.
*Lösung (Tradeoff-Options & KISS):* Das Blueprint darf keine widersprüchliche "Universal-Architektur" erfinden. Es muss solche architektonischen Diskrepanzen in klare **Pfade (Options)** trennen. Es präsentiert dem User im Dokument: *"Deine Literatur ist architektonisch gespalten. Option A (Monolith, C++) oder Option B (Microservices, Fullstack). Da S.A.G.E. das KISS-Prinzip für MVPs erzwingt, empfehle ich Pfad A."*

### Schwäche 4: Das Fundamental-Vakuum (Missing Baseline)
*Problem:* Extrem nischige Quellen (z. B. ein Paper über "Advanced Order Flow Dynamics") setzen die absoluten Basis-Systeme (Datenbankverwaltung, API-Verbindung zur Börse, Scheduling) als "gegeben" voraus und erwähnen diese mit keinem Wort. Konstruiert der Agent das MVP nur strikt nach diesen isolierten Dokumenten, entsteht ein Bot, der fantastische Mathematik kann, aber keine Orders absetzen und empfangen kann, weil diese Schichten "vergessen" wurden.
*Lösung (Baseline & Overlay):* Der `/blueprint-domain` Workflow und der MVP-Prompter werden so erweitert, dass der Agent sein existierendes KI-Weltwissen nicht abschaltet, sondern in **zwei Architekturschichten** arbeitet:
1. **Die Baseline (LLM Weltwissen):** Zuerst skizziert der Agent aus sich selbst heraus die absoluten Grundkomponenten für die Projektart (bei einem Trading Bot z. B. DB, Rest-Client, Heartbeat-Scheduler), die für jede Software unerlässlich sind.
2. **Das Architektur-Delta (Quellenwissen):** Erst dann legt er die aus den Nischen-Dokumenten extrahierten Expertensysteme als "Specialized Overlay" auf die Baseline. So ist das MVP am Ende eine Kombination aus S.A.G.E.-Standardarchitektur (die funktioniert) und radikalen Nischen-Zusätzen (die Profite generieren).

## 6. Fazit
Durch dieses intelligente Zweischritt-System (erst Makro-Strategie lesen, dann MVP kreieren, dann dediziertes Mikro-Wissen extrahieren) behält S.A.G.E. seine Strenge. Nutzer betreiben faktisch **Literatur-basiertes Reverse Engineering**, um Architektur-Standards einer völlig fremden Industrie nahtlos in sauberen Code zu übersetzen.
