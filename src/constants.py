from enum import Enum

class FileStatus(Enum):
        NONE = 0
        PARSED = 1   
        SPLITTED = 2
        READY_TO_UPLOAD = 3
        UPLOADED = 4

FILM_FILE_EXTENSION = ".mkv"

class LogColor:
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'
        endcolor = '\033[0m'

# TMBD_LOG_COLOR = LogColor.
# FILE_SPLITTER_LOG_COLOR = 
# TELEGRAM_LOG_COLOR = 

TELEGRAM_MAX_FILE_SIZE = 4000 * 1024 * 1024