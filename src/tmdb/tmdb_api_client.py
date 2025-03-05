import os
import time
import threading
import tmdbsimple as tmdb
from globals import movies_vector, mutex
from constants import FileStatus, LogColor
from utils import no_more_items
from movie import Movie
from .tmdb_constants import LANGUAGE, LANGUAGE_ENG, GENRES, POSTER_BASE_URL

API_KEY = os.getenv('API_KEY')

class TmdbClient(threading.Thread):
    def __init__(self):
        tmdb.API_KEY = API_KEY
        threading.Thread.__init__(self)

    def __parse_genres(self, genres: dict):
        parsed = []
        for genre in genres:
            parsed.append(GENRES[genre])
        return parsed

    def get_tmdb_data(self, movie: Movie):
        try:
            film = tmdb.Movies(movie.tmdb_id)
            film_info = film.info(language=LANGUAGE)

            title = film_info['title']
            year = film_info['release_date'][:4]
            genres_ids = [genre['id'] for genre in film_info['genres']]
            genres = self.__parse_genres(genres_ids)
            poster_path = film_info['poster_path']
            poster = POSTER_BASE_URL + poster_path
            duration_min = film_info['runtime']

            film_orig_info = film.info(language=LANGUAGE_ENG)
            title_eng = film_orig_info['title']
            print(f"{LogColor.lightgreen}[TmbdClient] Info obtained for the movie {movie.tmdb_id} - {title}{LogColor.endcolor}")
            with mutex:
                movie.set_movie_metadata(title, title_eng, year, genres, duration_min, poster)
        except Exception as e:
            print(f"{LogColor.lightred}[TmdbClient] Error getting movie info: {e}{LogColor.endcolor}")
            return True
        
    def run(self):
        global movies_vector
        error = False
        while(no_more_items(movies_vector, FileStatus.NONE) and not error):
            for m in movies_vector:
                if m.status == FileStatus.NONE:
                    error = self.get_tmdb_data(m)
            time.sleep(1)
        print(f"{LogColor.lightgreen}[TmdbClient] Closing thread{LogColor.endcolor}")