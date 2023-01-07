from Media import Media

class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, genre, number_of_seasons, number_of_episodes):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre
        self.season = number_of_seasons
        self.episode = number_of_episodes

    # Methods
    def show_info(self):
        print(f"Name\t| Director\t| Genre\t| IMDB Score\t| Seasons\t| Episodes\t| Duration".expandtabs(12))
        print(f"--------------------" * 5)
        print(f"{self.name}\t| {self.director}\t| {self.genre}\t| {self.imdb_score}\t| {self.season}\t| {self.episode}\t| {self.duration}".expandtabs(12))
        self.show_actors()