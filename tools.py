from langchain.tools import Tool
from datetime import datetime
import requests


#CALCULATOR TOOL
def calculator(expression: str) -> str:
    """
    Used to resolve mathematical expressions.
    Input example: '128 * 46'
    """
    try:
        result = eval(expression, {"__builtins__": {}})
        return str(result)
    except Exception:
        return "Erro ao calcular a expressão"


calculator_tool = Tool(
    name= "Calculator",
    func= calculator,
    description= (
        "Use this tool to solve mathematical expressions. The input must be a valid expression, e.g., '128 * 46'."
    ),
)


#DATETIME TOOL
def get_current_datetime(date: str = "") -> str:
    """
    Returns the current date and time.
    """

    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


datetime_tool = Tool(
    name= "CurrentDateTime",
    func= get_current_datetime,
    description=(
        "Use this tool for any question related to the current date or time,including today, yesterday, tomorrow, or the current day of the week."
    ),
)

#WEATHER TOOL
def get_weather(city: str)-> str:
    """
    Get current weather for a given city.
    Input example: 'São Paulo'
    """
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    geo_resp = requests.get(geo_url, params={"name": city, "count": 1})

    if geo_resp.status_code != 200 or not geo_resp.json().get("results"):
        return "City not found."
    
    location = geo_resp.json()["results"][0]
    lat, lon = location["latitude"], location["longitude"]

    # Weather
    weather_url = "https://api.open-meteo.com/v1/forecast"
    weather_resp = requests.get(
        weather_url,
        params={
            "latitude": lat,
            "longitude": lon,
            "current_weather": True
        }
    )

    if weather_resp.status_code != 200:
        return "Could not fetch weather data."

    weather = weather_resp.json()["current_weather"]
    temp = weather["temperature"]
    wind = weather["windspeed"]

    return f"Current temperature in {city}: {temp}°C, wind speed: {wind} km/h"

weather_tool = Tool(
    name="Weather",
    func=get_weather,
    description=(
        "Use this tool to get the current weather for a given city. "
        "The input should be a city name, e.g., 'São Paulo'."
    ),
)




