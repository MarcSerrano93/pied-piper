import os
import threading
from globals import movies_vector, mutex
from constants import FILM_FILE_EXTENSION
from movie import Movie

class FolderReader(threading.Thread):
    def __init__(self, folder_path : str):
        self.folder_path = folder_path
        threading.Thread.__init__(self)

    def run(self):
        global movies_vector
        for entry in os.scandir(self.folder_path):
            if (entry.is_file()):
                if entry.name.endswith(FILM_FILE_EXTENSION):
                    with mutex:
                        movies_vector.append(Movie(os.path.join(self.folder_path, entry.name)))