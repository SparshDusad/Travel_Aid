import requests, os
from dotenv import load_dotenv

load_dotenv()

def get_weather_summary(city: str):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"http://api.weatherapi.com/v1/forecast.json?q={city}&days=5&key={api_key}"
    response = requests.get(url).json()
    
    forecast = response.get("forecast", {}).get("forecastday", [])
    if not forecast:
        return ""
    
    summary = []
    for day in forecast:
        date = day["date"]
        condition = day["day"]["condition"]["text"]
        summary.append(f"{date}: {condition}")
    
    return " | ".join(summary)
