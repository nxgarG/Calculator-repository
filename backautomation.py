import tkinter as tk
import os
import shutil

window = tk.Tk()
window.title('Backup Automation')

label = tk.Label(window)
label.grid(row=0, column=0)

source, destination, name, extensions = '', '', 'no name', []

source_entry = tk.Entry(label, width=28)
source_entry.grid(row=0, column=0)


def source_command():
    global source
    source = source_entry.get()
    destination_entry.focus()


source_button = tk.Button(label, text='Confirm', command=source_command)
source_button.grid(row=0, column=1)

destination_entry = tk.Entry(label, width=28, )
destination_entry.grid(row=1, column=0)


def destination_command():
    global destination
    destination = destination_entry.get()
    extensions_entry.focus()


destination_button = tk.Button(label, text='Confirm', command=destination_command)
destination_button.grid(row=1, column=1)

extensions_entry = tk.Entry(label, width=28)
extensions_entry.grid(row=2, column=0)


def extensions_command():
    global extensions
    extensions = extensions_entry.get()
    name_entry.focus()


extensions_button = tk.Button(label, text='Confirm', command=extensions_command)
extensions_button.grid(row=2, column=1)

name_entry = tk.Entry(label, width=28)
name_entry.grid(row=3, column=0)


def name_command():
    global name
    name = name_entry.get()


name_button = tk.Button(label, text='Confirm', command=name_command)
name_button.grid(row=3, column=1)


def backup(src, dst, exts):
    global name
    for extension in exts:
        for dirpath, dirname, files in os.walk(src):
            del dirpath, dirname
            for file in files:
                if file.endswith(extension):
                    file_path = os.path.join(src, file)
                    finale_destination = dst + '/' + extension
                    if not os.path.exists(finale_destination):
                        os.mkdir(finale_destination)
                    shutil.copy(file_path, finale_destination)
    os.chdir(dst)
    shutil.make_archive(name, 'zip')


def command():
    global source, destination, extensions
    backup(source, destination, extensions)


backup_button = tk.Button(label, text='Backup Now', command=command)
backup_button.grid(row=4, column=0)

source_entry.focus()

window.mainloop()

print()
