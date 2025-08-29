from dotenv import load_dotenv
import requests
import os

load_dotenv()  # Load variables from .env file

# Read API key from environment variable
API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if not API_KEY:
        print("❌ API Key not found. Please set OPENWEATHER_API_KEY environment variable.")
        return

    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        city_name = data["name"]
        country = data["sys"]["country"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]

        print(f"📍 {city_name}, {country}")
        print(f"🌡 Temperature: {temp}°C")
        print(f"💧 Humidity: {humidity}%")
        print(f"☁ Weather: {weather}")
    else:
        print("❌ City not found!")

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
