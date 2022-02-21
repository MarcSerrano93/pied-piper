import os
import shutil

class FolderDeleter():

    def __init__(self, path) -> None:
        self.path = path

    def delete(self):
        folders = list(os.walk(self.path))[1:]
        for folder in folders:
            shutil.rmtree(folder[0], ignore_errors=True)