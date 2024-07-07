import os
import subprocess
   
class Film:
    def __init__(self, full_path):
        self.full_path = full_path
        self.is_splitted = False
    
    def getName(self):
        return self.name
    
    def getTmdbId(self):
        return self.tmdb_id
    
    def getYear(self):
        return self.year
    
    def isSplitted(self):
        return self.is_splitted
    
    def setISplitted(self, is_splitted):
        self.is_splitted = is_splitted

    def getZipName(self):
        return self.name + " (" + self.year + ").zip"
    
    def getTelegramCoverMessage(self):
        #ToDo
        return "🎬| " + self.getName() + "\n" + "📆| "+ self.getYear() + "\n" + "🎭| #Drama"
    
    def setFilmCategories(self, categories):
        #ToDo
        pass

    def splitFilm(self, dst_folder, max_fragment_size):
        base_name = os.path.basename(self.full_path).rsplit('.', 1)[0] # Remove extension
        tmdb_id = base_name.rsplit('{', 1) [1][:-1].rsplit('-',1)[1] # Get the tmdb id (only the number)
        year = base_name.rsplit('(', 1)[1].rsplit('{',1)[0][:-2] # Get the year (we remove 2 character to delete the ')' and an extra space
        name = base_name.rsplit('(', 1)[0] # Get the name of the film

        print(base_name)
        print(tmdb_id)
        print(year)
        print(name)
        print("=========")
        splitCommand = "../7z.exe a -v" + str(max_fragment_size) +"m "+ "\"" +dst_folder + "/" + name + " ("+ year + ").zip\"" + " " + "\"" +self.full_path + "\""
        print(splitCommand)
        print("Starting")
        process_output = subprocess.run(splitCommand) 
        print("Finishing")
        print (process_output.__dict__.get('returncode'))


if __name__ == "__main__":
    pass