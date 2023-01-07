from media import Media


class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, genre, casts):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre
    
    #Methods
    @staticmethod
    def show_table():
        print(f"Name\t| Director\t| Genre\t| IMDB Score\t| Duration(min)".expandtabs(12))
        print(f"---------------" * 5)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t| {self.genre}\t| {self.imdb_score}\t| {self.duration}".expandtabs(12))
        self.show_actors()