import json
import os

#JSON KEYS
SOURCE_FILES_PATH = "source_files_path"
DESTINATION_FILES_PATH = "destination_files_path"
MAX_FRAGMENT_SIZE = "max_fragment_size"
TELEGRAM_FILM_ENTITY_ID = "telegram_film_entity_id"

class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.source_files_path = config[SOURCE_FILES_PATH]
            if not self.source_files_path[-1] == '/':
                self.source_files_path = ''.join((self.source_files_path,'/')) 
                print(self.source_files_path)
            self.destination_files_path = config[DESTINATION_FILES_PATH]
            if not self.destination_files_path[-1] == '/':
                self.destination_files_path = ''.join((self.destination_files_path,'/')) 
                print(self.source_files_path)
            self.max_fragment_size = config[MAX_FRAGMENT_SIZE]
            self.telegram_film_entity_id = config[TELEGRAM_FILM_ENTITY_ID]
            print("CONFIG")
    
    def validate(self, force_dst_creation):
        if not os.path.exists(self.source_files_path):
            return False
        if not os.path.exists(self.destination_files_path):
            if force_dst_creation:
                os.makedirs(self.destination_files_path)
            else:
                return False
        if not self.max_fragment_size:
            return False
        if not self.telegram_film_entity_id:
            return False
        return True
            
    
    

if __name__ == "__main__":
    conf = Config()
    print(conf.get_source_files_path())
    print(conf.get_destination_files_path())
    print(conf.get_max_fragment_size())