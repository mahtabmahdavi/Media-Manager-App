from media import Media
from actors import Actor


class Series(Media):
    def __init__(self, name, director, imdb_score, url, duration, casts, genre, number_of_seasons, number_of_episodes):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, casts)
        self.genre = genre
        self.season = number_of_seasons
        self.episode = number_of_episodes

    #Methods
    @staticmethod
    def add(series_list):
        temp_name = input("\nName: ")
        temp_director = input("Director: ")
        temp_genre = input("Genre: ")
        temp_imdb_score = input("IMDB Score: ")
        temp_season = input("Number of Seasons: ")
        temp_episode = input("Number of Episodes: ")
        temp_duration = input("Duration(min): ")
        temp_url = input("URL: ")

        actors = []
        temp_actor = input("Actors(Press # to complete the process):\n")
        while temp_actor != "#":
            temp_actor = temp_actor.split(" ")
            actors.append(Actor(temp_actor[0], temp_actor[1]))
            temp_actor = input()

        series_obj = Series(temp_name, temp_director, temp_imdb_score, temp_url, temp_duration, actors, temp_genre, temp_season, temp_episode)
        if series_obj not in series_list:
            series_list.append(series_obj)

    @staticmethod
    def edit(series_list):
        edit_name = input("\nEnter the name of Series you want to edit: ")
        for item in series_list:
            if item.name == edit_name:
                print("\nWhich parts do you want to edit? ")
                print("1. Director")
                print("2. Genre")
                print("3. IMDB Score")
                print("4. Seasons")
                print("5. Episodes")
                print("6. Duration")
                print("7. URL")
                edit_choice = int(input("--> "))

                if edit_choice == 1:
                    item.director = input("\nDirector: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 2:
                    item.genre = input("\nGenre: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 3:
                    item.imdb_score = input("\nIMDB Score: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 4:
                    item.season = input("\nNumber of Seasons: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 5:
                    item.episode = input("\nNumber of Episodes: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 6:
                    item.duration = input("\nDuration: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                elif edit_choice == 7:
                    item.url = input("\nURL: ")
                    print("Information updated successfully!\n")
                    Series.show_table()
                    item.show_info()
                    break
                else:
                    print("\nThat's wrong! Try again.")
                    break
        else:
            print("\nThe Series was NOT found to edit.")

    @staticmethod
    def remove(series_list):
        remove_name = input("\nEnter the name of Series you want to remove: ")
        for item in series_list:
            if item.name == remove_name:
                print()
                Series.show_table()
                item.show_info()
                remove_choice = input("\nAre you sure? y/n ").lower()
                if remove_choice == "y":
                    series_list.remove(item)
                    print("\nYour Series has been removed successfully!")
                    break
                elif remove_choice == "n":
                    break
                else:
                    print("\nYour request has not been defined!")
                    break
        else:
            print("\nThe Series was NOT found to remove.")

    @staticmethod
    def search(series_list):
        search_name = input("\nEnter the name of Series you want: ")
        for item in series_list:
            if item.name == search_name:
                print("\nThe Series was found.\n")
                Series.show_table()
                item.show_info()
                break 
        else:
            print("\nThe Series was NOT found.")

    @staticmethod
    def show_table():
        print(f"Name\t|".expandtabs(20), end = "")
        print(f" Director\t|".expandtabs(30), end = "")
        print(f" Genre\t| IMDB Score\t| Seasons\t| Episodes\t| Duration".expandtabs(14))
        print(f"------------------" * 7)

    def show_info(self):
        print(f"{self.name}\t|".expandtabs(20), end = "")
        print(f" {self.director}\t|".expandtabs(30), end = "")
        print(f" {self.genre}\t| {self.imdb_score}\t| {self.season}\t| {self.episode}\t| {self.duration}".expandtabs(14))
        self.show_actors()

    def show_actors(self):
        print("\nActors:")
        for actor in self.casts:
            actor.show_info()