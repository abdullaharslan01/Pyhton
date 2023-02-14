import json
import os

class Person:
    def __init__(self,nameParam,surnameParam,phoneParam) -> None:
        self.name=nameParam
        self.surname=surnameParam
        self.phonenumber=phoneParam
    

    def readToFile()->list:
        
        if os.path.isfile("data.json"):
            with open("data.json","r") as fileObject:
                mylist=json.loads(json.load(fileObject))
        else:
            mylist=[]
        return mylist


    def insertToFile(self)->None:
        kisiler=Person.readToFile()
        kisilerdict=dict(name=self.name,surname=self.surname,phonenumber=self.phonenumber)
        kisiler.append(kisilerdict)
        with open("data.json","w") as fileObject:
            kisilerdums=json.dumps(kisiler)
            json.dump(kisilerdums,fileObject)
        
        print("Kisi Basariyle Kaydedildi")
    
    def kisiOku()->None:
        kisiler=Person.readToFile()
        print(f"{'Name':10}  {'Surname':10}  {'Phone':10}\n")
        
        for kisi in kisiler:
            print(f"{kisi['name']:10.10}  {kisi['surname']:10.10}  {kisi['phonenumber']:10.10}")
    
    def degisiklikleriKaydet(kisiler):
        with open("data.json","w") as fileObject:
            json.dump(json.dumps(kisiler),fileObject)


    def kisiSil()->None:
        kisiler=Person.readToFile()
        Person.kisiOku()
        print("")
        numara=input("What Number Do you want to delete: ")
        state=False
        for kisi in kisiler:
            if kisi["phonenumber"]==numara:
                kisiler.remove(kisi)
                Person.degisiklikleriKaydet(kisiler)
                state=True
                break

        if state==True:
            print("Kisi Basariyle Silindi...")
        else:
            print("Kisi Bulunamadi...")
        state=False
            
        


while True:
    print("")
    print("Kisiler".center(50,"*"))
    
    choice=input("1- Kisiler\n2- Kisi Ekle\n3- Kisi Sil\n4- Exit\nYour Choice: ")
    if choice=="4":
        break
    else:
        if choice=="1":
            Person.kisiOku()

        elif choice=="2":
            name=input("Name: ")
            surname=input("Surname: ")
            phonenumber=input("Phone Number: ")
            p1=Person(nameParam=name,surnameParam=surname,phoneParam=phonenumber)
            p1.insertToFile()
            print("")
        
        elif choice=="3":
            Person.kisiSil()
        
        else:
            print("Yanlis Secim Yaptiniz:(")