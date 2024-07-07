import json

#JSON KEYS
SOURCE_FILES_PATH = "source_files_path"
DESTINATION_FILES_PATH = "destination_files_path"
MAX_FRAGMENT_SIZE = "max_fragment_size"

class Config:
    def __init__(self):
        with open('config.json', 'r') as f:
            config = json.load(f)
            self.source_files_path = config[SOURCE_FILES_PATH]
            self.destination_files_path = config[DESTINATION_FILES_PATH]
            self.max_fragment_size = config[MAX_FRAGMENT_SIZE]
    
    def getSourceFilesPath(self):
        return self.source_files_path
    
    def getDestinationFilesPath(self):
        return self.destination_files_path
    
    def getMaxFragmentSize(self):
        return self.max_fragment_size
    

if __name__ == "__main__":
    conf = Config()
    print(conf.getSourceFilesPath())
    print(conf.getDestinationFilesPath())
    print(conf.getMaxFragmentSize())