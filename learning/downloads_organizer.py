import shutil
from pathlib import Path

base_path = Path(input("Enter path to organize: ")).expanduser().resolve()
if not base_path.exists():
    raise FileNotFoundError("That Folder does not exist.")

# Downloads = Path.home() / "Downloads"
entries = list(base_path.iterdir())

folder_count = 0
coding_count = 0
pdf_count = 0
office_files = 0
text_count = 0
images_count = 0
videos_count = 0
audio_count = 0
setup_count = 0
other_types = 0

BASE = base_path 

Pdfs   = BASE / "PDFs"
Office = BASE / "Office files"
text   = BASE / "Text files"
images = BASE / "Images"
videos = BASE / "Videos"
audio  = BASE / "Audio files"
coding = BASE / "Coding Files"
setup  = BASE / "Setups"

for folder in [Pdfs, Office, text, images, videos, audio, coding, setup]:
    folder.mkdir(exist_ok=True)
       
def file_move(destination: Path, source: Path):
    target = destination / source.name
    if not target.exists():
        shutil.move(source, target)
        print(f"Moved {source.name} -> {destination}")
        return
    
    counter = 1
    while True:
        new_name = f"{source.name}({counter}){source.suffix}"
        target = destination / new_name
        if not target.exists():
            shutil.move(source, target)
            print(f"Moved {source.name} -> {new_name}")
            break
        counter += 1


print("\n")
for entry in entries:
    if entry.is_dir():
        folder_count += 1
    else:
        ext = entry.suffix.lower()
        if ext == ".pdf":
            pdf_count += 1
            file_move(Pdfs, entry)

        elif ext == ".docx" or ext == ".xlsx" or ext == ".pptx" or ext == ".accdb":
            office_files += 1
            file_move(Office, entry)

        elif ext in (".csv", ".json", ".txt", ".md"):
            text_count += 1
            file_move(text)

        elif ext in (".png", ".jpg", ".jpeg", ".ico"):
            images_count += 1
            file_move(images, entry)

        elif ext in (".mp4", ".mov", ".mkv", ".avi"):
            videos_count += 1
            file_move(videos, entry)

        elif ext in (".mp3", ".wav", ".m4a", ".acc"):
            audio_count += 1
            file_move(audio, entry)
        
        elif ext in (".py", ".ipynb", ".java", ".html", ".cpp"):
            coding_count += 1
            file_move(coding, entry)

        elif ext == ".exe":
            setup_count += 1
            file_move(setup, entry)

        else:
            other_types += 1


print(
    f"{base_path} contain:\n"
    f"Total files: {len(entries)}\n"
    f"Subfolders: {folder_count}\n"
    f"Office files: {office_files}\n"
    f"Text files: {text_count}\n"
    f"Images: {images_count}\n"
    f"Videos {videos_count}\n"
    f"Audio {audio_count}\n"
    f"Coding files {coding_count}\n"
    f"Setup files {setup_count}\n"
    f"Other files: {other_types}"
    f"\nEverything Organized ;)\n"
)
