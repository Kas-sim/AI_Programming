import shutil
from pathlib import Path
from config import BASE, CATEGORIES

BASE = Path(input("Enter folder you want to organize: ")).expanduser().resolve()
if not BASE.exists():
    raise FileNotFoundError("This Folder does not exist.")

entries = list(BASE.iterdir())
folder_count = 0
other_types = 0

for category in CATEGORIES.values():
    category["folder"].mkdir(exist_ok=True)

required_keys = {"folder", "ext", "count"}

for name, category in CATEGORIES.items():
    missing = required_keys - category.keys
    if missing:
        raise KeyError(f"Category '{name}' missing keys: {missing}")
      
def file_move(destination: Path, source: Path):
    target = destination / source.name

    if not target.exists():
        shutil.move(source, target)
        print(f"Moved {source.name} -> {destination}")
        return

    counter = 1
    while True:
        new_name = f"{source.stem}({counter}){source.suffix}"
        target = destination / new_name
        if not target.exists():
            shutil.move(source, target)
            print(f"Moved {source.name} -> {new_name}")
            break
        counter += 1

DESTINATION_FOLDERS = {cat["folder"] for cat in CATEGORIES.values()}

for entry in entries:
    if entry.is_dir():
        if entry not in DESTINATION_FOLDERS:
            folder_count += 1
        continue

    ext = entry.suffix.lower()
    moved = False

    for category in CATEGORIES.values():
        if ext in category["ext"]:
            category["count"] += 1
            file_move(category["folder"], entry)
            moved = True
            break
    
    if not moved:
        other_types += 1

print(f"\n{BASE} contains:\n")
print(f"Total items: {len(entries)}")
print(f"Subfolders: {folder_count}")

for name, category in CATEGORIES.items():
    print(f"{name}: {category['count']}")

print(f"Other files: {other_types}")
print(f"\nEverything Organized :) \n")