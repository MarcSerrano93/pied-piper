import os
import time
import shutil
import threading
import subprocess
from globals import movies_vector, mutex
from constants import FileStatus, LogColor, TELEGRAM_MAX_FILE_SIZE
from utils import no_more_items
from movie import Movie

class FileSplitter(threading.Thread):
    def __init__(self, dst_folder : str, max_fragment_size : int):
        self.dst_parent_folder = dst_folder
        self.max_fragment_size = max_fragment_size
        threading.Thread.__init__(self)

    def split_file(self, movie : Movie):
        if not os.path.exists(self.dst_parent_folder):
            os.mkdir(self.dst_parent_folder) 

        dst_path = os.path.join(self.dst_parent_folder, movie.tmdb_id) 
        if os.path.exists(dst_path):
           shutil.rmtree(dst_path)
        
        os.makedirs(dst_path)
        
        file_size = os.path.getsize(movie.file_full_path)
        if (file_size > TELEGRAM_MAX_FILE_SIZE):
            zzip_path = os.path.abspath("7z.exe")
            splitCommand = f"\"{zzip_path}\" a -v{self.max_fragment_size}m \"{dst_path}/{movie.title} ({movie.year}).zip\" \"{movie.file_full_path}\""
            process_output = subprocess.run(splitCommand)
            print(f"{LogColor.pink}[FileSplitter] File: \"{os.path.basename(movie.file_full_path)}\" splitted{LogColor.endcolor}")
        else:
            shutil.move(movie.file_full_path, os.path.join(dst_path, os.path.basename(movie.file_full_path)))
            print(f"{LogColor.pink}[FileSplitter] File: \"{os.path.basename(movie.file_full_path)}\" moved{LogColor.endcolor}")

        with mutex:
            movie.splitted_path = dst_path
            movie.status = FileStatus.SPLITTED
    

    def run(self):
        global movies_vector
        error = False
        while(no_more_items(movies_vector, FileStatus.PARSED) and not error):
            for f in movies_vector:
                if f.status == FileStatus.PARSED:
                    error = self.split_file(f)
                    print(error)
            time.sleep(1)
        print(f"{LogColor.pink}[FileSplitter] Closing thread{LogColor.endcolor}")