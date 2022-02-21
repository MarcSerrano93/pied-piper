import os

EXTENSION = '.mkv'

class MkvRenamer:

    def __init__(self, name, new_name, origin_path, destination_path) -> None:
        self.name = name
        self.new_name = new_name
        self.origin_path = origin_path
        self.destination_path = destination_path
    
    def rename(self):
        os.rename(
            os.path.join(self.origin_path, self.name), 
            os.path.join(self.destination_path, self.new_name + EXTENSION))