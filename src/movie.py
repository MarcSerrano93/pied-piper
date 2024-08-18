from constants import FileStatus

class Movie:
    def __init__(self, file_full_path):
        self.file_full_path = file_full_path
        self.splitted_path = ""
        self.title = ""
        self.year = ""
        self.tmdb_id = self.get_tmdb_id_from_path()
        self.genres = []
        self.poster_path = ""
        self.status = FileStatus.NONE
        
    def get_tmdb_id_from_path(self):
        return self.file_full_path.rsplit('.', 1)[0].rsplit('{', 1)[1][:-1].rsplit('-',1)[1] # Get the tmdb id (only the number)
    
    def set_movie_metadata(self, title, year, genres, poster_path):
        self.title = title.replace(':', '.')
        self.year = year
        self.genres = genres
        self.poster_path = poster_path
        self.status = FileStatus.PARSED

    def generate_telegram_poster_caption(self):
        genres = self.genres[slice(5)]
        title = f"🎬| [{self.title}](themoviedb.org/movie/{self.tmdb_id})"
        year = self.year.replace('1', 'I').replace('0', 'O')
        year_str = f"📆| #{year}"
        genres_str = ""
        for g in genres:
            genres_str += f"\n🎭| #{g}"
        caption = f"{title}\n{year_str}{genres_str}"
        return caption
    
    def generate_telegram_poster_caption_old(self):
        genres = self.genres[slice(5)]
        title = f"🎬| {self.title}"
        year = self.year.replace('1', 'I').replace('0', 'O')
        year_str = f"📆| #{year}"
        genres_str = ""
        for g in genres:
            genres_str += f"\n🎭| #{g}"
        id = f"🎟| #{self.tmdb_id}"
        caption = f"{title}\n{year_str}{genres_str}\n{id}"
        return caption
    
    def __repr__(self):
        return (
            f"Movie(\n"
            f"    id={self.tmdb_id},\n"
            f"    name='{self.title}',\n"
            f"    year='{self.year}',\n"
            f"    poster_path='{self.poster_path}',\n"
            f"    genres='{self.genres}',\n"
            f")"
        )
            
if __name__ == "__main__":
    movie = Movie("C:\Peliculas\Movie (2024) {tmdb-112233}.mkv")
    print(movie.tmdb_id)
    print(movie.title)
    movie.set_movie_metadata("Bad Boys. Ride or Die", "2018", ['Drama', 'Accion'], "")
    print(movie.generate_telegram_poster_caption_old())