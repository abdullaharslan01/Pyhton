import requests
import time
import re

class Film:
    def __init__(self) -> None:
        self.loop=True

    def program(self):
        choice=self.menu()

        if choice=="1":
            self.top250()
        if choice=="2":
            self.mostPopuler()
        if choice=="3":
            self.intheaters()
        if choice=="4":
            self.soonaspossible()
        if choice=="5":
            self.searchFilm()
        if choice=="6":
            self.aboutme()
        if choice=="7":
            self.exit()
        

    def menu(self):
        def control(choice):
            if re.search("[^1-7]",choice):
                raise Exception("Wrong Choose! Please Choose [1-6]")

        while True:
            try:
                print("")
                print(f"{'Welcome to TheaTronDB by Abdullah Arslan':*^60}")
                choice=input("\n\nPlease choose one of the options above...\n\n[1]- Top 250 movies\n[2]- Most popular movies\n[3]- In Theaters\n[4]- Coming Soon\n[5]- Search A Film\n[6]- About Developer\n[7]- Exit\n\n[Choice]: ")
                control(choice=choice)
            except Exception as fail:
                print(fail)
                time.sleep(2)
            else:
                break
        return choice
                
        
    def top250(self):
        print("Reaching the list of top 250 movies...\n\n")
        URL="https://imdb-api.com/en/API/Top250Movies/k_ohru4xqa"
        time.sleep(2)
        response=requests.get(URL).json()

        print(f"{'Rank':<8} {'Film Name and Date':<75} {'Rating':<3}\n")
        for film in response["items"]:
            print(f'{film["rank"]:<8}- {film["fullTitle"]:<75} {film["imDbRating"]:<3}')

        self.menuloop()

    def mostPopuler(self):
        print("Reaching the list of most populer movies...\n\n")
        URL="https://imdb-api.com/en/API/MostPopularMovies/k_ohru4xqa"
        time.sleep(2)
        response=requests.get(URL).json()

        print(f"{'Rank':<8} {'Film Name and Date':<75} {'Rating':<3}\n")
        for film in response["items"]:
            print(f'{film["rank"]:<8}- {film["fullTitle"]:<75} {film["imDbRating"]:<3}')

        self.menuloop()

    def intheaters(self):
        print("Reaching the list of in theaters movies now...\n\n")
        URL="https://imdb-api.com/en/API/InTheaters/k_ohru4xqa"
        time.sleep(2)
        response=requests.get(URL).json()
        print(f"{'Rank':<8} {'Film Name and Date':<75} {'Rating':<3}\n")
        counter=1
        for film in response["items"]:
            print(f'{counter:<8}- {film["fullTitle"]:<75} {film["imDbRating"]:<3}')
            counter+=1
        counter=1

        self.menuloop()


    def soonaspossible(self):
        print("Reaching the list of in Coming Soon movies now...",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".\n")
        
        URL="https://imdb-api.com/en/API/ComingSoon/k_ohru4xqa"
        response=requests.get(URL).json()
        print(f"{'Rank':<8} {'Film Name and Date':<75} {'Realese State':<20}\n")
        counter=1
        for film in response["items"]:
            print(f'{counter:<8}- {film["fullTitle"]:<75} {film["releaseState"]:<20}')
            counter+=1
        counter=1

        self.menuloop()



    def searchFilm(self):
        print("Reaching the menu of searching a film.",end="")
        time.sleep(1)
        print(".",end="")
        time.sleep(1)
        print(".\n")
        
        state=True
        while state:
            try:    
                TOP250URL="https://imdb-api.com/en/API/Top250Movies/k_ohru4xqa"
                response=requests.get(TOP250URL).json()
                filmname=input('Enter the movie name you want to search: ')
                filmid=""
                for film in response["items"]:
                    if film["title"]==filmname:
                        filmid=film["id"]

                URL="https://imdb-api.com/API/Wikipedia/k_ohru4xqa/"+filmid
                response=requests.get(URL).json()
                print(f'\nTitle: {response["fullTitle"]:<20}\n\nDescription: {response["plotShort"]["plainText"]}\n')
            except:
                print(f"Unfortunateley {filmname} not found!\n")
            finally:
                cont=input("Do you want to search again? Yes(1) or No(0): ")
                print(" ")
                if cont=="0":
                    break

        self.menuloop()



    def exit(self):
        print("See you later as soon as possible. Exitting...")
        time.sleep(2)
        self.loop=False
        exit()

    def aboutme(self):
        print("")
        print("About Me: Hello, I'm Abdullah. I am from Turkey. I am a computer engineering student. I'm into data science. I share my projects\n")
        print("How did I find the program name: The name of the program comes from the word Theatron. According to one view; thea means goddess and tron means place, so we reach the meaning of the house of the goddess. According to this view, theater in ancient Greece was not a theater but a purely religious ritual. There are various discussions and theses on this subject. In short: the word meaning the place of sight, the place where something is seen. The word theater is derived from here.")
        print("it's TheaTronDB\n")
        self.menuloop()

    def menuloop(self):
        while True:
            x=input("Press (8) to return to the main menu. Press (7) to exit: ")
            if x=="8":
                print("Returning to main menu")
                time.sleep(3)
                self.program()
                break
            elif x=="7":
                self.exit()
            else:
                print("Please make a valid choice")
            

System=Film()

while System.loop:
    System.program()