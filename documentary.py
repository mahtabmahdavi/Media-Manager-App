from media import Media


class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, topic):
        # Properties
        super().__init__(name, director, imdb_score, url, duration)
        self.topic = topic
    
    # Methods
    @staticmethod
    def show_table():
        print(f"Name\t| Director\t| Topic\t| IMDB Score\t| Duration(min)".expandtabs(12))
        print(f"---------------" * 5)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t| {self.topic}\t| {self.imdb_score}\t| {self.duration}".expandtabs(12))