import os
import PySimpleGUI as App
from modules.zipCreator import makeArchive, ExtractFile

compress_column = [
    [App.Text("Select Files: "), App.InputText(), App.FilesBrowse("Select", key="files")],
    # [App.Text("Select Folder: "), App.InputText(), App.FolderBrowse("Select", key="folder")],
    [App.Button("Compress", key="Compress"), App.Text(key="output")]
]

extract_column = [
    [App.Text("Select Zip File: "), App.InputText(), App.FileBrowse("Select", key="zip_file")],
    # [App.Text("Select Folder: "), App.InputText(), App.FolderBrowse("Select", key="zip_folder")],
    [App.Button("Extract", key="Extract"), App.Text(key="output2")]
]
# list of layouts
layouts = [
    [App.Text("COMPRESS FILES:", font=14)],
    [compress_column],
    [App.Text("")],
    [App.HSeparator()],
    [App.Text("")],
    [App.Text("EXTRACT FILE:", font=14)],
    [extract_column]
]

window = App.Window("CompressMaster", layout=layouts)
while True:
    event, values = window.read()
    if event == App.WIN_CLOSED:
        break
    elif event == "Compress":
        file_paths = values["files"].split(";")
        folder_path = os.path.dirname(file_paths[0])
        makeArchive(file_paths, folder_path)
        window['output'].update(value="Successfully Compressed!")
    elif event == "Extract":
        zip_file_path = values["zip_file"]
        zip_folder_path = os.path.dirname(zip_file_path)
        ExtractFile(zip_file_path, zip_folder_path)
        window['output2'].update(value="File successfully Extracted!")

window.close()
