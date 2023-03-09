import zipfile
import pathlib


def makeArchive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "Compresses.zip")
    with zipfile.ZipFile(dest_path, "w") as file:
        for filepath in filepaths:
            file.write(filepath)


def ExtractFile(filepath, dest_dir):
    with zipfile.ZipFile(filepath, "r") as archive:
        archive.extractall(dest_dir)
