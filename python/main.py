import os
from tkinter import Tk
from tkinter import filedialog

from application.MkvRenamer import MkvRenamer
from application.FolderDeleter import FolderDeleter

def main():
    origin = ask_path()
    destination = ask_path()

    folders = list(os.walk(origin))
    index = 0
    for folder in folders:
        for file in folder[2]:
            if file.endswith('.mkv'):
                MkvRenamer(file, folders[0][1][index], folder[0], destination).rename()
                index += 1
    FolderDeleter(origin).delete()

def ask_path():
    Tk().withdraw()
    return filedialog.askdirectory()

if __name__ == "__main__":
    main()