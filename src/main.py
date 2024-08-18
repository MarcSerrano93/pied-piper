from config import Config
from folder_reader import FolderReader
from tmdb.tmdb_api_client import TmdbClient
from file_splitter import FileSplitter
from telegram.telegram_api_client import TelegramAPIClient

from constants import LogColor

def main():
    config = Config()
    if not config.validate(force_dst_creation=False):
        print("Invalid config file")
        return
    readDir = FolderReader(config.source_files_path)
    readDir.start()
    readDir.join()

    tmdbClient = TmdbClient()
    tmdbClient.start()

    fileSplitter = FileSplitter(config.destination_files_path, config.max_fragment_size)
    fileSplitter.start()

    telegramClient = TelegramAPIClient(config.telegram_film_entity_id)
    telegramClient.start()

    tmdbClient.join()
    fileSplitter.join()
    telegramClient.join()

if __name__ == "__main__":
    main()