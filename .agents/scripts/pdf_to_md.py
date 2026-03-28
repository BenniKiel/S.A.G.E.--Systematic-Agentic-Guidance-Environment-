import sys
import os

def convert_pdf_to_md(pdf_path):
    try:
        import pymupdf4llm  # type: ignore
    except ImportError:
        print("Fehler: Das Paket 'pymupdf4llm' ist nicht installiert.")
        print("Bitte installiere es in deiner Arbeitsumgebung mit:")
        print("pip install pymupdf4llm")
        sys.exit(1)

    if not os.path.exists(pdf_path):
        print(f"Fehler: Angegebene PDF-Datei nicht gefunden: {pdf_path}")
        sys.exit(1)
        
    print(f"[*] Konvertiere {pdf_path} zu Markdown...")
    try:
        # Führt die Extraktion von Texten, Tabellen und Layouts durch
        md_text = pymupdf4llm.to_markdown(pdf_path)
        
        # Erstellt einen gleichnamigen .md Pfad im selben Verzeichnis
        out_path = os.path.splitext(pdf_path)[0] + ".md"
        
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md_text)
            
        print(f"[+] Erfolg! Die Markdown-Rohtext-Datei wurde gespeichert unter: {out_path}")
    except Exception as e:
        print(f"[-] Ein Fehler ist bei der Konvertierung aufgetreten: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python pdf_to_md.py <path_to_pdf>")
        print("Example: python .agents/scripts/pdf_to_md.py .agents/knowledge/_raw/book.pdf")
        sys.exit(1)
        
    pdf_path = sys.argv[1]
    convert_pdf_to_md(pdf_path)
