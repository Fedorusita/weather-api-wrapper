from dotenv import dotenv_values
import httpx



def get_weather(city:str) -> dict:
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}"

    config = dotenv_values(".env")
    api_key = config["VISUAL_CROSSING_API_KEY"]

    params = {
    "unitGroup": "metric",
    "include": "current",
    "contentType": "json",
    "key": api_key
    }

    response = httpx.get(url, params=params, timeout=10.0)
    response.raise_for_status()

    data = response.json()

    current = data["currentConditions"]

    temperature = current["temp"]
    condition = current["conditions"]

    result = {
        "city": city, 
        "temperature":  temperature,
        "condition": condition
    }
    
    return result
