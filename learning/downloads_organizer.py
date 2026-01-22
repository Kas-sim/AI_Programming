import shutil
from pathlib import Path

folder = Path("D:/Downloads")
entries = list(folder.iterdir())

print(f"{folder} contains {len(entries)} files!\n")

pdf_count = 0
doc_count = 0
csv_count = 0
text_count = 0
images_count = 0
folder_count = 0
other_types = 0


for entry in entries:
    if entry.is_dir():
        folder_count += 1
    else:
        ext = entry.suffix.lower()
        if ext == ".pdf":
            pdf_count += 1

            Pdfs = Path("D:/Downloads/PDFs")
            Pdfs.mkdir(parents=True, exist_ok=True)
            shutil.move(entry, Pdfs)

        elif ext == ".docx":
            doc_count += 1
        elif ext == ".csv":
            csv_count += 1
        elif ext in (".png", ".jpg", ".jpeg"):
            images_count += 1
        elif ext in (".txt", ".md"):
            text_count += 1
        else:
            other_types += 1

print(
    f"Total files: {len(entries)}\n"
    f"Subfolders: {folder_count}\n"
    f"Pdfs: {pdf_count}\n"
    f"Word files: {doc_count}\n"
    f"Text files: {text_count}\n"
    f"CSV files: {csv_count}\n"
    f"Images: {images_count}\n"
    f"Other files: {other_types}"
)
