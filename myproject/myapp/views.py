from django.shortcuts import render
import requests
from decouple import config
import os

API_KEY = config("OPENWEATHER_API_KEY")
print("API_KEY:", API_KEY)  

def home(request):
    city = request.GET.get("city")
    weather = None

    if city:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
        response = requests.get(url)
    
        if response.status_code == 200:
            data = response.json()
            weather = {
                "city": data["name"],
                "temperature": data["main"]["temp"],
                "description": data["weather"][0]["description"],
                "icon": data["weather"][0]["icon"]
            }
        else:
            weather = {"Error": "Could not fetch weather data"} 

    return render(request, "home.html", {"weather": weather})
