from media import Media


class Documentary(Media):
    def __init__(self, name, director, imdb_score, url, duration, topic):
        # Properties
        super().__init__(name, director, imdb_score, url, duration, [])
        self.topic = topic
    
    #Methods
    @staticmethod
    def add(documentary_list):
        temp_name = input("\nName: ")
        temp_director = input("Director: ")
        temp_topic = input("Topic: ")
        temp_imdb_score = input("IMDB Score: ")
        temp_duration = input("Duration(min): ")
        temp_url = input("URL: ")

        documentary_obj = Documentary(temp_name, temp_director, temp_imdb_score, temp_url, temp_duration, temp_topic)
        if documentary_obj not in documentary_list:
            documentary_list.append(documentary_obj)

    @staticmethod
    def edit(documentary_list):
        edit_name = input("\nEnter the name of Documentary you want to edit: ")
        for item in documentary_list:
            if item.name == edit_name:
                print("\nWhich parts do you want to edit? ")
                print("1. Director")
                print("2. Topic")
                print("3. IMDB Score")
                print("4. Duration")
                print("5. URL")
                edit_choice = int(input("--> "))

                if edit_choice == 1:
                    item.director = input("\nDirector: ")
                    print("Information updated successfully!\n")
                    Documentary.show_table()
                    item.show_info()
                    break
                elif edit_choice == 2:
                    item.topic = input("\nTopic: ")
                    print("Information updated successfully!\n")
                    Documentary.show_table()
                    item.show_info()
                    break
                elif edit_choice == 3:
                    item.imdb_score = input("\nIMDB Score: ")
                    print("Information updated successfully!\n")
                    Documentary.show_table()
                    item.show_info()
                    break
                elif edit_choice == 4:
                    item.duration = input("\nDuration: ")
                    print("Information updated successfully!\n")
                    Documentary.show_table()
                    item.show_info()
                    break
                elif edit_choice == 5:
                    item.url = input("\nURL: ")
                    print("Information updated successfully!\n")
                    Documentary.show_table()
                    item.show_info()
                    break
                else:
                    print("\nThat's wrong! Try again.")
                    break
        else:
            print("\nThe Documentary was NOT found to edit.")

    @staticmethod
    def remove(documentary_list):
        remove_name = input("\nEnter the name of Documentary you want to remove: ")
        for item in documentary_list:
            if item.name == remove_name:
                print()
                Documentary.show_table()
                item.show_info()
                remove_choice = input("\nAre you sure? y/n ").lower()
                if remove_choice == "y":
                    documentary_list.remove(item)
                    print("\nYour documentary has been removed successfully!")
                    break
                elif remove_choice == "n":
                    break
                else:
                    print("\nYour request has not been defined!")
                    break
        else:
            print("\nThe Documentary was NOT found to remove.")

    @staticmethod
    def search(documentary_list):
        search_name = input("\nEnter the name of Documentary you want: ")
        for item in documentary_list:
            if item.name == search_name:
                print("\nThe Documentary was found.\n")
                Documentary.show_table()
                item.show_info()
                break 
        else:
            print("\nThe Documentary was NOT found.")

    @staticmethod
    def show_table():
        print(f"Name\t| Director\t|".expandtabs(22), end = "")
        print(f" Topic\t| IMDB Score\t| Duration(min)".expandtabs(14))
        print(f"------------------" * 5)
        
    def show_info(self):
        print(f"{self.name}\t| {self.director}\t|".expandtabs(22), end = "")
        print(f" {self.topic}\t| {self.imdb_score}\t| {self.duration}".expandtabs(14))