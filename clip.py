from media import Media
from actors import Actor


class Clip(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, genre):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre
    
    #Methods
    @staticmethod
    def add(clip_list):
        temp_name = input("\nName: ")
        temp_director = input("Director: ")
        temp_genre = input("Genre: ")
        temp_imdb_score = input("IMDB Score: ")
        temp_duration = input("Duration(min): ")
        temp_url = input("URL: ")

        actors = []
        temp_actor = input("Actors(Press # to complete the process):\n")
        while temp_actor != "#":
            temp_actor = temp_actor.split(" ")
            actors.append(Actor(temp_actor[0], temp_actor[1]))
            temp_actor = input()

        clip_obj = Clip(temp_name, temp_director, temp_imdb_score, temp_url, temp_duration, actors, temp_genre)
        if clip_obj not in clip_list:
            clip_list.append(clip_obj)

    @staticmethod
    def edit(clip_list):
        edit_name = input("\nEnter the name of Clip you want to edit: ")
        for item in clip_list:
            if item.name == edit_name:
                print("\nWhich parts do you want to edit? ")
                print("1. Director")
                print("2. Genre")
                print("3. IMDB Score")
                print("4. Duration")
                print("5. URL")
                edit_choice = int(input("--> "))

                if edit_choice == 1:
                    item.director = input("\nDirector: ")
                    print("Information updated successfully!\n")
                    Clip.show_table()
                    item.show_info()
                    break
                elif edit_choice == 2:
                    item.genre = input("\nGenre: ")
                    print("Information updated successfully!\n")
                    Clip.show_table()
                    item.show_info()
                    break
                elif edit_choice == 3:
                    item.imdb_score = input("\nIMDB Score: ")
                    print("Information updated successfully!\n")
                    Clip.show_table()
                    item.show_info()
                    break
                elif edit_choice == 4:
                    item.duration = input("\nDuration: ")
                    print("Information updated successfully!\n")
                    Clip.show_table()
                    item.show_info()
                    break
                elif edit_choice == 5:
                    item.url = input("\nURL: ")
                    print("Information updated successfully!\n")
                    Clip.show_table()
                    item.show_info()
                    break
                else:
                    print("\nThat's wrong! Try again.")
                    break
        else:
            print("\nThe Clip was NOT found to edit.")

    @staticmethod
    def remove(clip_list):
        remove_name = input("\nEnter the name of Clip you want to remove: ")
        for item in clip_list:
            if item.name == remove_name:
                print()
                Clip.show_table()
                item.show_info()
                remove_choice = input("\nAre you sure? y/n ").lower()
                if remove_choice == "y":
                    clip_list.remove(item)
                    print("\nYour Clip has been removed successfully!")
                    break
                elif remove_choice == "n":
                    break
                else:
                    print("\nYour request has not been defined!")
                    break
        else:
            print("\nThe Clip was NOT found to remove.")

    @staticmethod
    def search(clip_list):
        search_name = input("\nEnter the name of Clip you want: ")
        for item in clip_list:
            if item.name == search_name:
                print("\nThe Clip was found.\n")
                Clip.show_table()
                item.show_info()
                break 
        else:
            print("\nThe Clip was NOT found.")

    @staticmethod
    def show_table():
        print(f"Name\t| Director\t|".expandtabs(20), end = "")
        print(f" Genre\t| IMDB Score\t| Duration(min)".expandtabs(14))
        print(f"------------------" * 5)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t|".expandtabs(20), end = "")
        print(f" {self.genre}\t| {self.imdb_score}\t| {self.duration}".expandtabs(14))
        self.show_actors()

    def show_actors(self):
        print("\nActors:")
        for actor in self.casts:
            actor.show_info()