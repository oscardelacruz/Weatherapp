import requests
#CREATE ACCOUNT AND INSER API KEY HERE
API_KEY = "----------------------"

user_input = input("Enter City: ")

weather_data  = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={API_KEY}")

weather = weather_data.json()['weather'][0]['main']
temp = round(weather_data.json()['main']['temp'])

print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}°F")







