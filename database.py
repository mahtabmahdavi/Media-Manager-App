from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actors import Actor


class DataBase:
    def __init__(self, type, path):
        # Properties
        self.type = type
        self.path = path

    # Methods
    def read_from_database(self, media_list):
        with open("./Database/" + self.path, "r") as file:
            for line in file:
                temp_file = line[:-1].split(",")
                actors = []

                if self.type == "Film":
                    for i in range(5, len(temp_file) - 1):
                        temp_actor = temp_file[i].split(" ")
                        actors.append(Actor(temp_actor[0], temp_actor[1]))
                    film_obj = Film(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], actors, temp_file[len(temp_file) - 1])
                    media_list.append(film_obj)

                elif self.type == "Series":
                    for i in range(5, len(temp_file) - 3):
                        temp_actor = temp_file[i].split(" ")
                        actors.append(Actor(temp_actor[0], temp_actor[1]))
                    series_obj = Series(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], actors, temp_file[len(temp_file) - 3], temp_file[len(temp_file) - 2], temp_file[len(temp_file) - 1])
                    media_list.append(series_obj)
                
                elif self.type == "Documentary":
                    documentary_obj = Documentary(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], temp_file[5])
                    media_list.append(documentary_obj)

                elif self.type == "Clip":
                    for i in range(5, len(temp_file) - 1):
                        temp_actor = temp_file[i].split(" ")
                        actors.append(Actor(temp_actor[0], temp_actor[1]))
                    clip_obj = Clip(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], actors, temp_file[len(temp_file) - 1])
                    media_list.append(clip_obj)
    
    def write_to_database(self, media_list):
        file = open("./Database/" + self.path, "w")
        for item in media_list:
            if self.type == "Film":
                file.write(f"{item.name},{item.director},{item.imdb_score},{item.url},{item.duration},")
                for i in range(len(item.casts)):
                    file.write(f"{item.casts[i].first_name} {item.casts[i].last_name},")
                file.write(f"{item.genre}\n")

            elif self.type == "Series":
                file.write(f"{item.name},{item.director},{item.imdb_score},{item.url},{item.duration},")
                for i in range(len(item.casts)):
                    file.write(f"{item.casts[i].first_name} {item.casts[i].last_name},")
                file.write(f"{item.genre},{item.season},{item.episode}\n")

            elif self.type == "Documentary":
                file.write(f"{item.name},{item.director},{item.imdb_score},{item.url},{item.duration},{item.topic}\n")

            elif self.type == "Clip":
                file.write(f"{item.name},{item.director},{item.imdb_score},{item.url},{item.duration},")
                for i in range(len(item.casts)):
                    file.write(f"{item.casts[i].first_name} {item.casts[i].last_name},")
                file.write(f"{item.genre}\n")
        file.close()