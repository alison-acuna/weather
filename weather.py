# Exercise: Command-Line Weather
# For this exercise you will create a command-line program that asks
# "Where should I check the weather?" and responds
# "The weather in {location} is {fahrenheit}° F".


import requests

city = input("Where should I check the weather? Please use the format city,country ")

r = requests.get("{}{}{}".format("http://api.openweathermap.org/data/2.5/weather?q=", city, "&APPID=02eb5ea0b486efc9dccb386a405b1702&response=json"))
temp = (r.json()['main']['temp'])
temp_f = 1.8 * (temp - 273) + 32.
print(temp_f)
