import os
import pathlib as path

folder = "D:\\Downloads"
entries = os.listdir(folder)

print(f"{folder} contains {len(entries)} files!\n")

pdf_count = 0
doc_count = 0
csv_count = 0
other_types = 0

for file in entries:
    extention = path.Path(file).suffix
    if extention == ".pdf":
        pdf_count += 1
    elif extention == ".docx":
        doc_count += 1
    elif extention == ".csv":
        csv_count += 1
    else:
        other_types += 1
        
print(f"Total files: {len(entries)} \nPdfs: {pdf_count} \nWord files: {doc_count} \nCSV files: {csv_count}\n Other files: {other_types}")
