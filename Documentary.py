from Media import Media

class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, topic):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.topic = topic
    
    # Methods
    def show_info(self):
        print(f"Name\t| Director\t| Topic\t| IMDB Score\t| Duration".expandtabs(12))
        print(f"---------------" * 5)
        print(f"{self.name}\t| {self.director}\t| {self.topic}\t| {self.imdb_score}\t| {self.duration}".expandtabs(12))