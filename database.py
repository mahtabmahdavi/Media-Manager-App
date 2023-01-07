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
                temp_actor = []
                if self.type == "Film":
                    for i in range(6, len(temp_file)):
                        temp_actor.append(temp_file[i])
                    film_obj = Film(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], temp_file[5],temp_actor)
                    media_list.append(film_obj)

                elif self.type == "Series":
                    for i in range(8, len(temp_file)):
                        temp_actor.append(temp_file[i])
                    series_obj = Series(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], temp_file[5], temp_file[6], temp_file[7],temp_actor)
                    media_list.append(series_obj)
                
                elif self.type == "Documentary":
                    documentary_obj = Documentary(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], temp_file[5])
                    media_list.append(documentary_obj)

                elif self.type == "Clip":
                    for i in range(6, len(temp_file)):
                        temp_actor.append(temp_file[i])
                    clip_obj = Clip(temp_file[0], temp_file[1], temp_file[2], temp_file[3], temp_file[4], temp_file[5],temp_actor)
                    media_list.append(clip_obj)
    
    def write_to_database(self, media_list):
        file = open("./Database/" + self.path, "w")
        for item in media_list:
            if self.type == "Film":
                file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]},")
                for i in range(len(item[6])):
                    if i == len(item[6] - 1):
                        file.write(f"{item[6][i]}\n")
                    else:
                        file.write(f"{item[6][i]},")

            elif self.type == "Series":
                file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]},{item[6]},{item[7]},")
                for i in range(len(item[7])):
                    if i == len(item[7] - 1):
                        file.write(f"{item[7][i]}\n")
                    else:
                        file.write(f"{item[7][i]},")

            elif self.type == "Documentary":
                file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]}\n")

            elif self.type == "Clip":
                file.write(f"{item[0]},{item[1]},{item[2]},{item[3]},{item[4]},{item[5]},")
                for i in range(len(item[6])):
                    if i == len(item[6] - 1):
                        file.write(f"{item[6][i]}\n")
                    else:
                        file.write(f"{item[6][i]},")  
        file.close()