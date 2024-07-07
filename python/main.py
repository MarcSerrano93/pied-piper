import os

from application.Config import Config
from application.Film import Film

FILM_FILE_EXTENSION = ".mkv"

def main():
    config = Config()
    films = []
    for file in os.listdir(config.getSourceFilesPath()):
        if file.endswith(FILM_FILE_EXTENSION):
            films.append(Film(config.getSourceFilesPath() + "/" + file))

    for film in films:
        film.splitFilm(config.getDestinationFilesPath(), config.getMaxFragmentSize())
    

if __name__ == "__main__":
    main()