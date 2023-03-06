import PySimpleGUI as App
from modules.zipCreator import makeArchive

label1 = App.Text("Select Files: ")
input1 = App.InputText()
choose_files = App.FilesBrowse("Select", key="files")
label2 = App.Text("Select Folder: ")
input2 = App.InputText()
select_folder = App.FolderBrowse("Select", key="folder")
compress_button = App.Button("Compress")
output = App.Text(key="output")

# list of layouts
layouts = [[label1, input1, choose_files], [label2, input2, select_folder], [compress_button, output]]

window = App.Window("CompressMaster", layout=layouts)
while True:
    event, values = window.read()
    file_paths = values["files"].split(";")
    folder_path = values["folder"]
    makeArchive(file_paths, folder_path)
    window['output'].update(value="Successfully Compresses!")
    if event == App.WIN_CLOSED:
        break


window.close()
