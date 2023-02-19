import requests
import re
from bs4 import BeautifulSoup

class Coin:
    def __init__(self) -> None:
        self.State=True
        self.Counter=1
        self.aboutme()
    
    def aboutme(self):
        print("\n")
        print("About Me: Hello, I'm Abdullah. I am from Turkey. I am a computer engineering student. I'm into data science. I share my projects\n")
        print("How did I find the program name: Ploutos is the Roman god of abundance and wealth. Coin means money. By combining the two. I found the name CoinTos :)\n")
        print("it's CoinTos\n")
        print("Note: The data comes instantly from crypto.com. For more detailed information, you can go to https://crypto.com/price \n\n")


    def Program(self):
        page=self.menu()
        self.n_First_Data(page)
        self.Counter=1
        self.mainMenu()
    
    def close_Program(self):
        exit()
    
    def mainMenu(self):
        choice=input("Press 1 to return to the main page, press any key to exit: ")
        if choice=="1":
            self.Program()
        else:
            self.close_Program()
    
    def menu(self):
        def control(choice):
            if re.findall("[^1-9]",choice):
                raise Exception(f"""
                        {'':☣<55}
                        ☣ Wrong choice please enter a value between [1]-[293] ☣
                        {'':☣<55}

                
                """)
            elif not 0<int(choice)<294:
                raise Exception(f"Wrong choice please enter a value between [1]-[293]")
        
        while True:
            try:
                choice=input(f"""
             {'':✴<76}
            ✴ You can display up to 293 pages. You can view around 14684 coins in total. ✴ 
             {'':✴<76}
 
                            {'':❆<41}
                            ❆ Press 1 for the first 50    coin data ❆
                            ❆ Press 2 for the first 100   coin data ❆
                            ❆ Press 3 for the first 150   coin data ❆
                            ❆ Press n for the first 50*n  coin data ❆
                            {'':❆<41}

[Your Choice]: """) 
                control(choice)
            except Exception as fail:
                print(fail)
            else:
                break
        return choice


    def n_First_Data(self,page):
        print(f"{'Rank':<10} {'Coin Name':<40} {'Coin Price':<20} {'Coin Market Cap':<40}\n")
        for page in range(1,int(page)+1):
            self.datas(page)
        print("\n")
        
    def datas(self,page):
        URL=f"https://crypto.com/price?page={page}"
        soup=BeautifulSoup(requests.get(URL).content,"html.parser")
        
        my_Data=soup.find_all("tr",{'class':'css-1cxc880'})
        coin_Name=list()
        coin_Price=list()
        coin_Market_Cap=list()
        for data in my_Data:
            coin_Name.append(data.find("td",{"class":"css-1sem0fc"}).a.div.find("div",{"class":"css-ttxvk0"}).p.text)

            coin_Price.append(data.find("div",{"class":"css-b1ilzc"}).text)

            coin_Market_Cap.append(data.find_all("td",{"class":"css-1nh9lk8"})[1].text)

        for index in range(len(coin_Name)):
            print(f"{self.Counter:<10} {coin_Name[index]:<40} {coin_Price[index]:<20} {coin_Market_Cap[index]:<40}")
            self.Counter+=1

        

        
program=Coin()

while program.State:
    program.Program()
