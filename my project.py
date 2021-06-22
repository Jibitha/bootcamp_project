import requests
#import os
from datetime import datetime

api_key = '6770f8b5df13e5af1705e8841d8564b8'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print("-------------------------------------------------------------")
print("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print("-------------------------------------------------------------")

print("Current temperature is: {:.2f}deg C".format(temp_city))
print("Current weather desc  : ",weather_desc)
print("Current Humidity      : ",hmdt,'%')
print("Current wind speed    : kmph".format(wind_spd))

x=open("my_project.txt",'a+')

x.write("-------------------------------------------------------------\n")
x.write("Weather Stats for - {}  || {}\n".format(location.upper(), date_time))
x.write("-------------------------------------------------------------\n")

x.write("Current temperature is: {:.2f} deg C\n".format(temp_city))
x.write("Current weather desc  :{} \n".format(weather_desc))
x.write("Current Humidity      :{} %\n".format(hmdt))
x.write("Current wind speed    :{} kmph\n".format(wind_spd))

x.close()

