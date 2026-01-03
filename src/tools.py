from langchain.tools import tool
from langchain.agents import Tool
from datetime import datetime
import requests
import math
import httpx


#CALCULATOR TOOL
def calculator(expression: str) -> str:
    """
    Used to resolve mathematical expressions.
    Input example: '128 * 46'
    """

    #
    allowed_names = {"sqrt": math.sqrt, "pi": math.pi, "sin": math.sin,"cos": math.cos, "tan": math.tan, "log": math.log}

    try:
        result = eval(expression, {"__builtins__": {}},allowed_names)
        return str(result)
    except Exception as e:
        return f"Error calculating the expression: {e}"


#Exemple of a Tool as a class
calculator_tool = Tool( 
    name= "Calculator",
    func= calculator,
    description= (
        "Tool used to solve mathematical expressions. The input must be a valid expression, e.g., '128 * 46'."
    ),
)


#Exemple of a Tool as a decorator
#DATETIME TOOL
@tool
def datetime_tool(date: str = "") -> str:
    """
    Used for any question related to the current date or time
    """

    now = datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


#Exemple of a async Tool
#WEATHER TOOL
@tool
async def weather_tool(city: str)-> str:
    """
    Get current weather for a given city.
    Input example: 'São Paulo'
    """
    geo_url = "https://geocoding-api.open-meteo.com/v1/search"
    weather_url = "https://api.open-meteo.com/v1/forecast"
    #geo_resp = requests.get(geo_url, params={"name": city, "count": 1})

    try:
        async with httpx.AsyncClient(timeout=10) as client:
            geo_resp = await client.get(geo_url,params={"name": city, "count": 1})
        geo_data = geo_resp.json()
        if not geo_data.get("results"):
            return "City not found."
        
        location = geo_data["results"][0]
        lat, lon = location["latitude"], location["longitude"]


        async with httpx.AsyncClient(timeout=10) as client:
            weather_resp = await client.get(
                weather_url,
                params={
                "latitude": lat,
                "longitude": lon,
                "current_weather": True
                }
            )
        weather_data =  weather_resp.json()
      #  if not weather_data.get("results"):
            #return "Weather not found."
        weather= weather_data["current_weather"]
        temp = weather["temperature"]
        wind = weather["windspeed"]

        return f"Current temperature in {city}: {temp}°C, wind speed: {wind} km/h"

    except Exception as e:
            return f"Error fetching weather: {e}"





