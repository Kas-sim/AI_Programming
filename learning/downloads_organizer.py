import shutil
from pathlib import Path

folder = Path("D:/Downloads")
entries = list(folder.iterdir())

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


Pdfs = Path("D:/Downloads/PDFs")
Pdfs.mkdir(parents=True, exist_ok=True)
Office = Path("D:/Downloads/Office files")
Office.mkdir(parents=True, exist_ok=True)
text = Path("D:/Downloads/Text files")
text.mkdir(parents=True, exist_ok=True)
images = Path("D:/Downloads/Images")
images.mkdir(parents=True, exist_ok=True)
videos = Path("D:/Downloads/Videos")
videos.mkdir(parents=True, exist_ok=True) 
audio = Path("D:/Downloads/Audio files")
audio.mkdir(parents=True, exist_ok=True) 
coding = Path("D:/Downloads/Coding Files")
coding.mkdir(parents=True, exist_ok=True) 
setup = Path("D:/Downloads/Setups")
setup.mkdir(parents=True, exist_ok=True)
        


for entry in entries:
    if entry.is_dir():
        folder_count += 1
    else:
        ext = entry.suffix.lower()
        if ext == ".pdf":
            pdf_count += 1
            shutil.move(entry, Pdfs)
            print(f"Moved {entry} -> {Pdfs}!")

        elif ext == ".docx" or ext == ".xlsx" or ext == ".pptx" or ext == ".accdb":
            office_files += 1
            shutil.move(entry, Office)
            print(f"Moved {entry} -> {Office}")

        elif ext in (".csv", ".json", ".txt", ".md"):
            text_count += 1

            shutil.move(entry, text)
            print(f"Moved {entry} -> {text}")

        elif ext in (".png", ".jpg", ".jpeg", ".ico"):
            images_count += 1

            shutil.move(entry, images)
            print(f"Moved {entry} -> {images}")
        
        elif ext in (".mp4", ".mov", ".mkv", ".avi"):
            videos_count += 1

            shutil.move(entry, videos)
            print(f"Moved {entry} -> {videos}")

        elif ext in (".mp3", ".wav", ".m4a", ".acc"):
            audio_count += 1

            shutil.move(entry, audio)
            print(f"Moved {entry} -> {audio}")
        
        elif ext in (".py", ".ipynb", ".java", ".html", ".cpp"):
            coding_count += 1

            shutil.move(entry, coding)
            print(f"Moved {entry} -> {coding}")

        elif ext == ".exe":
            setup_count += 1

            shutil.move(entry, setup)
            print(f"Moved {entry} -> {setup}")

        else:
            other_types += 1


print(
    f"\nEverything Organized ;)\n"
    f"\Downloads contain:\n"
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
)
