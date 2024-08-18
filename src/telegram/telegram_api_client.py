import threading
import asyncio
import time
import os
from telethon import TelegramClient
from telethon.tl.functions.channels import GetForumTopicsRequest
from FastTelethonhelper import fast_upload
from globals import mutex, movies_vector
from utils import no_more_items
from constants import FileStatus, LogColor
from movie import Movie
from .telegramConstants import API_ID, API_HASH

API_ID = os.getenv('API_ID')
API_HASH = os.getenv('API_HASH')
PHONE_NUMBER = os.getenv('PHONE_NUMBER')

class TelegramAPIClient(threading.Thread):
    def __init__(self, telegram_film_entity_id):
        self.telegram_film_entity_id = telegram_film_entity_id
        threading.Thread.__init__(self)

    def print_progress(self, current, total, title):
        progress_percent = int(100 * current / total)
        if progress_percent % 5 == 0:
            print(f"{LogColor.lightcyan}[TelegramAPIClient] Uploading {title}: {progress_percent}%{LogColor.endcolor}")
            

    async def get_existing_topics(self, client, channel_id):
        existing_topics = {}
        
        response = await client(GetForumTopicsRequest(
            channel=channel_id,
            offset_date=None,
            offset_id=0,
            offset_topic=0,
            limit=10000000,
        ))

        for topic in response.topics:
            existing_topics[topic.title] = topic

        return existing_topics

    async def upload_movie_to_telegram(self, client, supergroup, existing_topics, movie : Movie):
        topic = ""
        if f'{movie.title[0]}' in existing_topics:
            #print(f'Topic "{movie.title[0]}" already exists. Uploading files to this topic...')
            topic = existing_topics[f'{movie.title[0]}']
        if topic == "":
            print(f"{LogColor.lightred}[TelegramAPIClient] ERROR Topic doesn't exist{LogColor.endcolor}")

        await client.send_file(
            entity=supergroup,
            file=movie.poster_path,
            caption=movie.generate_telegram_poster_caption_old(),
            reply_to=topic.id
        )

        file_list = []
        for entry in os.scandir(movie.splitted_path):
            if entry.is_file():
                file_list.append(movie.splitted_path + "/" + entry.name)  # Solo usar el nombre del archivo

       # start_time = time.time()
        uploaded_files=[]
        for file in file_list:
            uploaded_file = await fast_upload(
                client,
                file,
                None,
                progress_bar_function=self.print_progress)
            uploaded_files.append(uploaded_file)
        
        # end_time = time.time()
        # elapsed_time = end_time - start_time
        # print("Tiempo de ejecución:", elapsed_time, "segundos")

        await client.send_file(
            entity=supergroup,
            file=uploaded_files,
            progress_callback=lambda current, total: self.print_progress(current, total, movie.title),
            reply_to=topic.id
        )

        print(f"{LogColor.lightcyan}[TelegramAPIClient] Movie: {movie.title} successfully uploaded to Telegram {LogColor.endcolor}")
        with mutex:
            movie.status = FileStatus.UPLOADED

    def run(self):
        global movies_vector
        async def inner(self):
            client = TelegramClient('uploader', API_ID, API_HASH)
            phone_number=PHONE_NUMBER
            await client.start(phone_number)
            try:
                supergroup = await client.get_entity(self.telegram_film_entity_id)
                existing_topics = await self.get_existing_topics(client, supergroup)
            except Exception as e:
                print(f"{LogColor.lightred}[TelegramAPIClient] Error retrieving the supergroup: {e}{LogColor.endcolor}")
                return
            while(no_more_items(movies_vector, FileStatus.SPLITTED)):
                for f in movies_vector:
                    if f.status == FileStatus.SPLITTED:
                        await self.upload_movie_to_telegram(client, supergroup, existing_topics, f)
                time.sleep(1)
            print(f"{LogColor.lightcyan}[TelegramAPIClient] Closing thread{LogColor.endcolor}")
            await client.disconnect()
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(inner(self))
        loop.close()