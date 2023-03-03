import PySimpleGUI as App

label1 = App.Text("Select Files: ")
input1 = App.InputText()
files = App.FilesBrowse("Select")
label2 = App.Text("Select Folder: ")
input2 = App.InputText()
folder = App.FolderBrowse("Select")
compress_button = App.Button("Compress")

# list of layouts
layouts = [[label1, input1, files], [label2, input2, folder], [compress_button]]

window = App.Window("CompressMaster App", layout=layouts)
window.read()
window.close()
