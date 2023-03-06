import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "Enter your api key" 
 # go to " https://openweathermap.org/ " sign up and get your api key (must wait atleast 2 hours to get your account fully registerd in oder to use the api key)
CITY = "London" #any city you desire 


def kelvin_to_celsius_fahrenheit(Kelvin):
    celsius = Kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32 
    return celsius, fahrenheit 

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response['main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature in {CITY}: {temp_celsius:.2f}°C or {temp_fahrenheit:.2f}°F")
print(f"Temperature in {CITY} feels like: {feels_like_celsius:.2f}°C or {feels_like_fahrenheit:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%") 
print(f"Wind speed in {CITY}: {wind_speed}m/s")
print(f"General weather in {CITY}: {description}")  
print(f"Sunrise in {CITY} at {sunrise_time} local time.")  
print(f"Sunset in {CITY} at {sunset_time} local time.")





