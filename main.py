import requests
import json
import pyttsx3

city=input("Enter the name of the city \n")

url=f"https://api.weatherapi.com/v1/current.json?key=b9357d49fce74a23ac963130251301&q={city}"
r=requests.get(url)
# print(r.text)
wdict=json.loads(r.text)
w=wdict["current"]["temp_c"]
engine=pyttsx3.init()
engine.say(f"the current weather in {city} is {w} degree")
engine.runAndWait()

