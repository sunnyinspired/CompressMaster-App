import zipfile
import pathlib


def makeArchive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compresses.zip")
    with zipfile.ZipFile(dest_path, "w") as file:
        for filepath in filepaths:
            file.write(filepath)
