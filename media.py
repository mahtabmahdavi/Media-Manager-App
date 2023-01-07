import pytube
from actors import Actor


class Media:
    def __init__(self, name, director, imdb_score, url, duration):
        # Properties
        self.name = name
        self.director = director
        self.imdb_score = imdb_score
        self.url = url
        self.duration = duration
        self.casts = []

    #Methods
    @staticmethod
    def add():
        media_obj = Media()
        media_obj.name = input("\nName = ")
        media_obj.director = input("Director = ")
        media_obj.imdb_score = input("IMDB Score = ")
        media_obj.url = input("URL = ")
        media_obj.duration = input("Duration(min) = ")

        temp = input("Actors(Press # to complete the process) = ")
        while temp != "#":
            temp = temp.split(" ")
            media_obj.casts.append(Actor(temp[0], temp[1]))
        return media_obj

    def edit(media_list):
        edit_name = input("Enter the name of Media you want to remove: ")
        for item in media_list:
            if item.name == edit_name:
                print("\nWhich parts do you want to edit? ")
                print("1. Director")
                print("2. IMDB Score")
                print("3. URL")
                print("4. Duration")
                edit_choice = int(input("--> "))

                if edit_choice == 1:
                    item.director = input("Director = ")
                    print("\nInformation updated successfully!")
                    Media.show_table()
                    item.show_info
                    break
                elif edit_choice == 2:
                    item.imdb_score = input("IMDB Score = ")
                    print("\nInformation updated successfully!")
                    Media.show_table()
                    item.show_info
                    break
                elif edit_choice == 3:
                    item.url = input("URL = ")
                    print("\nInformation updated successfully!")
                    Media.show_table()
                    item.show_info
                    break
                elif edit_choice == 4:
                    item.duration = input("Duration = ")
                    print("\nInformation updated successfully!")
                    Media.show_table()
                    item.show_info
                    break
                else:
                    print("\nThat's wrong! Try again.")
                    break
        else:
            print("\nThe Media was NOT found to edit.")

    @staticmethod
    def remove(media_list):
        remove_name = input("Enter the name of Media you want to remove: ")
        for item in media_list:
            if item.name == remove_name:
                Media.show_table()
                item.show_info()

                remove_choice = input("Are you sure? y/n ").lower()
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
                print("\nThe Media was found.")
                Media.show_table()
                item.show_info()
                break 
        else:
            print("\nThe Media was NOT found.")

    @staticmethod
    def advanced_search(media_list):
        adv_list = []
        search_duration_1 = input("\nEnter your first duration in minutes: ")
        search_duration_2 = input("\nEnter your second duration in minutes: ")
        for item in media_list:
            if item.duration >= search_duration_1 and item.duration <= search_duration_2:
                adv_list.append(item)
                break 
        else:
            print("\nThe Media was NOT found.")
        return adv_list

    def download(self):
        media_stream = pytube.YouTube(self.url).streams.first()
        media_stream.download(output_path = "./Download/", filename = f"{self.name}.mp4")
  
    @staticmethod
    def show_table():
        print(f"Name\t| Director\t| IMDB Score\t| Duration(min)".expandtabs(12))
        print(f"----------------" * 4)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t| {self.genre}\t| {self.imdb_score}\t| {self.duration}".expandtabs(12))
        self.show_actors()