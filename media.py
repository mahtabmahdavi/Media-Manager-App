import pytube
from actors import Actor


class Media:
    def __init__(self, name, director, imdb_score, url, duration, casts):
        # Properties
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = casts

    #Methods
    @staticmethod
    def add(media_list):
        temp_name = input("\nName: ")
        temp_director = input("Director: ")
        temp_imdb_score = input("IMDB Score: ")
        temp_duration = input("Duration(min): ")
        temp_url = input("URL: ")

        actors = []
        temp_actor = input("Actors(Press # to complete the process):\n")
        while temp_actor != "#":
            temp_actor = temp_actor.split(" ")
            actors.append(Actor(temp_actor[0], temp_actor[1]))
            temp_actor = input()
            
        media_obj = Media(temp_name, temp_director, temp_imdb_score, temp_url, temp_duration, actors)
        if media_obj not in media_list:
            media_list.append(media_obj)

    @staticmethod
    def edit(media_list):
        edit_name = input("\nEnter the name of Media you want to edit: ")
        for item in media_list:
            if item.name == edit_name:
                print("\nWhich parts do you want to edit? ")
                print("1. Director")
                print("2. IMDB Score")
                print("3. Duration")
                print("4. URL")
                edit_choice = int(input("--> "))

                if edit_choice == 1:
                    item.director = input("\nDirector: ")
                    print("Information updated successfully!\n")
                    Media.show_table()
                    item.show_info()
                    break
                elif edit_choice == 2:
                    item.imdb_score = input("\nIMDB Score: ")
                    print("Information updated successfully!\n")
                    Media.show_table()
                    item.show_info()
                    break
                elif edit_choice == 3:
                    item.duration = input("\nDuration: ")
                    print("Information updated successfully!\n")
                    Media.show_table()
                    item.show_info()
                    break
                elif edit_choice == 4:
                    item.url = input("\nURL: ")
                    print("Information updated successfully!\n")
                    Media.show_table()
                    item.show_info()
                    break
                else:
                    print("\nThat's wrong! Try again.")
                    break
        else:
            print("\nThe Media was NOT found to edit.")

    @staticmethod
    def remove(media_list):
        remove_name = input("\nEnter the name of Media you want to remove: ")
        for item in media_list:
            if item.name == remove_name:
                print()
                Media.show_table()
                item.show_info()
                remove_choice = input("\nAre you sure? y/n ").lower()
                if remove_choice == "y":
                    media_list.remove(item)
                    print("\nYour Media has been removed successfully!")
                    break
                elif remove_choice == "n":
                    break
                else:
                    print("\nYour request has not been defined!")
                    break
        else:
            print("\nThe Media was NOT found to remove.")
  
    @staticmethod
    def search(media_list):
        search_name = input("\nEnter the name of Media you want: ")
        for item in media_list:
            if item.name == search_name:
                print("\nThe Media was found.\n")
                Media.show_table()
                item.show_info()
                break 
        else:
            print("\nThe Media was NOT found.")

    @staticmethod
    def advanced_search(media_list):
        advanced_list = []
        search_duration_1 = int(input("\nEnter your first duration in minutes: "))
        search_duration_2 = int(input("Enter your second duration in minutes: "))
        for item in media_list:
            if int(item.duration) >= search_duration_1 and int(item.duration) <= search_duration_2:
                advanced_list.append(item)
        return advanced_list

    def download(self):
        media_stream = pytube.YouTube(self.url).streams.first()
        media_stream.download(output_path = "./Download/", filename = f"{self.name}.mp4")
  
    @staticmethod
    def show_table():
        print(f"Name\t| Director\t| IMDB Score\t| Duration(min)".expandtabs(12))
        print(f"----------------" * 4)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t| {self.imdb_score}\t| {self.duration}".expandtabs(12))