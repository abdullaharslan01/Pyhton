import requests

print(f"{' Welcome To Weatheus by Abdullah Arslan ':*^90}\n\nNotice: The data comes instantly from openweathermap.org\n")
while True:
    city=input("Please enter the name of the city you want to know the weather forecast for(Exit:(0)): ")
    if city=="0" or city=="":
        print("Thank you for using the Weatheus Program. I wish you healthy days.")
        break
    else:
        try:    
            myapikey="6a885dce66575ac87f22c963dc4f8bdc"
            url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={myapikey}&units=metric"
            result=requests.get(url).json()
            weather=result["weather"][0]["description"]
            temp=result["main"]["temp"]
            feels_like=result["main"]["feels_like"]
            mintemp=result["main"]["temp_min"]
            maxtemp=result["main"]["temp_max"]
            pressure=result["main"]["pressure"]
            humidity=result["main"]["humidity"]
            print("\n")
            info=f"*{city.title()} Weather Temperature Information is as follows...*"
            print(f"{'':*^{len(info)}}")
            print(info)
            print(f"{'':*^{len(info)}}")
            print(f"*Tempature: {temp}°\n*Weather: {weather}\n*Felt Temperature: {feels_like}°\n*Min Tempature: {mintemp}°\n*Max Tempature: {maxtemp}°\n*Pressure: {pressure}hpa\n*Humidity: {humidity}%")
            print(f"{'':*^{len(info)}}\n")
        except KeyError as Fail:
            print(f'\n"{city} city was not found. Please enter a valid city! \n')