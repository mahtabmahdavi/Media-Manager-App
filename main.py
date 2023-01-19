import pyfiglet
from media import Media
from database import DataBase
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip
from actors import Actor


def section_menu():
    print("1. Film")
    print("2. Series")
    print("3. Documentary")
    print("4. Clip")
    return input("--> ")

def function_menu():
    print("\n1. Add")
    print("2. Edit")
    print("3. Remove")
    print("4. Search")
    print("5. Advanced Search")
    print("6. Download")
    print("7. Show list")
    print("8. Exit")
    return input("--> ")

def film_handler(function_request):
    if function_request == "1":
        Film.add(FILMS)

    elif function_request == "2":
        Film.edit(FILMS)

    elif function_request == "3":
        Film.remove(FILMS)

    elif function_request == "4":
        Film.search(FILMS)

    elif function_request == "5":
        result = Film.advanced_search(FILMS)
        if len(result) > 0:    
            for item in result:
                print()
                Film.show_table()
                item.show_info() 
        else:
            print("\nNothing was found!")

    elif function_request == "6":
        download_name = input("\nName: ")
        download_director = input("Director: ")
        for item in FILMS:
            if item.name == download_name and item.director == download_director:
                item.download()
                print("\nYour Film has been downloaded successfully!")
                break
        else:
            print("\nThe Film was NOT found to download.")

    elif function_request == "7":
        for item in FILMS:
            print()
            Film.show_table()
            item.show_info()
                    
    elif function_request == "8":
        db_film.write_to_database(FILMS)
        exit()

    else:
        print("\nThe input isn't valid.\nTry again!")


def series_handler(function_request):
    if function_request == "1":
        Series.add(SERIES)
        
    elif function_request == "2":
        Series.edit(SERIES)
        
    elif function_request == "3":
        Series.remove(SERIES)

    elif function_request == "4":
        Series.search(SERIES)

    elif function_request == "5":
        result = Series.advanced_search(SERIES)
        if len(result) > 0:    
            for item in result:
                print()
                Series.show_table()
                item.show_info() 
        else:
            print("\nNothing was found!")

    elif function_request == "6":
        download_name = input("\nName: ")
        download_director = input("Director: ")
        for item in SERIES:
            if item.name == download_name and item.director == download_director:
                item.download()
                print("\nYour Series has been downloaded successfully!")
                break
        else:
            print("\nThe Series was NOT found to download.")

    elif function_request == "7":
        for item in SERIES:
            print()
            Series.show_table()
            item.show_info()
                    
    elif function_request == "8":
        db_series.write_to_database(SERIES)
        exit()
    
    else:
        print("\nThe input isn't valid.\nTry again!")


def documentary_handler(function_request):
    if function_request == "1":
        Documentary.add(DOCUMENTARIES)
        
    elif function_request == "2":
        Documentary.edit(DOCUMENTARIES)
        
    elif function_request == "3":
        Documentary.remove(DOCUMENTARIES)

    elif function_request == "4":
        Documentary.search(DOCUMENTARIES)

    elif function_request == "5":
        result = Documentary.advanced_search(DOCUMENTARIES)
        if len(result) > 0:    
            for item in result:
                print()
                Documentary.show_table()
                item.show_info() 
        else:
            print("\nNothing was found!")

    elif function_request == "6":
        download_name = input("\nName: ")
        download_director = input("Director: ")
        for item in DOCUMENTARIES:
            if item.name == download_name and item.director == download_director:
                item.download()
                print("\nYour Documentary has been downloaded successfully!")
                break
        else:
            print("\nThe Documentary was NOT found to download.")

    elif function_request == "7":
        for item in DOCUMENTARIES:
            print()
            Documentary.show_table()
            item.show_info()
                    
    elif function_request == "8":
        db_documentary.write_to_database(DOCUMENTARIES)
        exit()

    else:
        print("\nThe input isn't valid.\nTry again!")


def clip_handler(function_request):
    if function_request == "1":
        Clip.add(CLIPS)

    elif function_request == "2":
        Clip.edit(CLIPS)
        
    elif function_request == "3":
        Clip.remove(CLIPS)

    elif function_request == "4":
        Clip.search(CLIPS)

    elif function_request == "5":
        result = Clip.advanced_search(CLIPS)
        if len(result) > 0:    
            for item in result:
                print()
                Film.show_table()
                item.show_info() 
        else:
            print("\nNothing was found!")

    elif function_request == "6":
        download_name = input("\nName: ")
        download_director = input("Director: ")
        for item in CLIPS:
            if item.name == download_name and item.director == download_director:
                item.download()
                print("\nYour Clip has been downloaded successfully!")
                break
        else:
            print("\nThe Clip was NOT found to download.")

    elif function_request == "7":
        for item in CLIPS:
            print()
            Clip.show_table()
            item.show_info()

    elif function_request == "8":
        db_clip.write_to_database(CLIPS)
        exit()
        
    else:
        print("\nThe input isn't valid.\nTry again!")


tittle = pyfiglet.figlet_format("Media Manager", font = "slant")
print(tittle)

FILMS = []
SERIES = []
DOCUMENTARIES = []
CLIPS = []

db_film = DataBase("Film", "films.txt")
db_series = DataBase("Series", "series.txt")
db_documentary = DataBase("Documentary", "documentaries.txt")
db_clip = DataBase("Clip", "clips.txt")

db_film.read_from_database(FILMS)
db_series.read_from_database(SERIES)
db_documentary.read_from_database(DOCUMENTARIES)
db_clip.read_from_database(CLIPS)

while True:
    print()
    section_choice = section_menu()
    if section_choice == "1":
        function_choice = function_menu()
        film_handler(function_choice)
    elif section_choice == "2":
        function_choice = function_menu()
        series_handler(function_choice)
    elif section_choice == "3":
        function_choice = function_menu()
        documentary_handler(function_choice)
    elif section_choice == "4":
        function_choice = function_menu()
        clip_handler(function_choice)        
    else:
        print("\nThe input isn't valid.\nTry again!")