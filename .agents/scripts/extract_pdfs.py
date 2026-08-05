import fitz
import os
import json

pdf_dir = "attached_assets"
files = sorted([f for f in os.listdir(pdf_dir) if f.endswith('.pdf')])

results = {}
for fname in files:
    path = os.path.join(pdf_dir, fname)
    doc = fitz.open(path)
    page_count = doc.page_count
    text = ""
    for i in range(page_count):
        page = doc[i]
        text += page.get_text() + "\n\n--- PAGE BREAK ---\n\n"
    doc.close()
    results[fname] = {"pages": page_count, "text": text}
    print(f"Extracted: {fname} ({page_count} pages, {len(text)} chars)")

with open(".agents/outputs/pdfs_text.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("\nDone!")
