import shutil
from pathlib import Path
from config import CATEGORIES_TEMPLATE

BASE = Path(input("Enter folder you want to organize: ")).expanduser().resolve()
if not BASE.exists() or not BASE.is_dir():
    raise FileNotFoundError("This Folder does not exist.")

CATEGORIES = {}

for name, data in CATEGORIES_TEMPLATE.items():
    CATEGORIES[name] = {
        "folder": BASE / data["folder"],
        "ext": data["ext"],
        "count": 0
    }

for category in CATEGORIES.values():
    category["folder"].mkdir(exist_ok=True)

folder_count = 0
other_types = 0

required_keys = {"folder", "ext", "count"}

for name, category in CATEGORIES.items():
    missing = required_keys - category.keys()
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

entries = list(BASE.iterdir())
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

for dstn in DESTINATION_FOLDERS:
    if dstn.exists() and dstn.is_dir() and not any(dstn.iterdir()):
        dstn.rmdir()


print(f"\n{BASE} contains:\n")
print(f"Total items: {len(entries)}")
print(f"Subfolders: {folder_count}")

for name, category in CATEGORIES.items():
    print(f"{name}: {category['count']}")

print(f"Other files: {other_types}")
print(f"\nEverything Organized :) \n")