import pathlib as path

folder = "Downloads"

for file in folder:
    if file == ".pdf":
        create("pdf")
        move file to folder/pdf