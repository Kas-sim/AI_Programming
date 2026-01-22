import shutil
from pathlib import Path

folder = Path("D:/Downloads")
entries = list(folder.iterdir())

print(f"{folder} contains {len(entries)} files!\n")

pdf_count = 0
office_files = 0
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
            print(f"Moved {entry} -> {Pdfs}!")

        elif ext == ".docx" or ext == ".xlsx" or ext == ".pptx" or ext == ".accdb":
            office_files += 1
            Office = Path("D:/Downloads/Office files")
            Office.mkdir(parents=True, exist_ok=True)
            shutil.move(entry, Office)
            print(f"Moved {entry} -> {Office}")

        elif ext in (".csv", ".json", ".txt", ".md"):
            text_count += 1

            text = Path("D:/Downloads/Text files")
            text.mkdir(parents=True, exist_ok=True)
            shutil.move(entry, text)
            print(f"Moved {entry} -> {text}")

        elif ext in (".png", ".jpg", ".jpeg"):
            images_count += 1
            images = Path("D:/Downloads/Images")
            images.mkdir(parents=True, exist_ok=True)
            shutil.move(entry, images)
            print(f"Moved {entry} -> {images}")

        else:
            other_types += 1

print(
    f"Total files: {len(entries)}\n"
    f"Subfolders: {folder_count}\n"
    f"Office files: {office_files}\n"
    f"Text files: {text_count}\n"
    f"Images: {images_count}\n"
    f"Other files: {other_types}"
)
