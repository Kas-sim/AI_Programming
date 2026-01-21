import os
import pathlib as path

folder = ("D:\\Downloads")
entries = os.listdir(folder)

print(f"{folder} contains {len(entries)} files!\n")

pdf_count = 0
doc_count = 0
csv_count = 0
images_count = 0
folder_count = 0
other_types = 0


for file in entries:

    full_path = os.path.join(folder, file)

    if os.path.isdir(full_path):
        folder_count += 1
    else:
        extention = path.Path(file).suffix
        if extention == ".pdf":
            pdf_count += 1
        elif extention == ".docx":
            doc_count += 1
        elif extention == ".csv":
            csv_count += 1
        elif extention == ".png" or extention == ".jpg" or extention == ".jpeg": 
            images_count += 1
        else:
            other_types += 1
        
print(f"Total files: {len(entries)} \nsubfolders: {folder_count}   \nPdfs: {pdf_count} \nWord files: {doc_count} \nCSV files: {csv_count} \nImages: {images_count} \nOther files: {other_types}")
