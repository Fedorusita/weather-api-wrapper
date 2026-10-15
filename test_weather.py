from dotenv import dotenv_values
import httpx
import sys


url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Moscow"

config = dotenv_values(".env")
api_key = config["VISUAL_CROSSING_API_KEY"]


params = {
    "unitGroup": "metric",
    "include": "current",
    "contentType": "json",
    "key": api_key
}
try:
    response = httpx.get(url, params=params, timeout=10.0)
    response.raise_for_status()
except httpx.HTTPStatusError as exc:
    print(f"Ошибка HTTP: {exc.response.status_code}")
    sys.exit()
except httpx.ConnectError as exc:
    print(f"Ошибка HTTP: {exc}")
    sys.exit()
except httpx.TimeoutException as exc:
    print(f"Ошибка HTTP: {exc}")
    sys.exit()
except httpx.RequestError as exc:
    print(f"Ошибка HTTP: {exc}")
    sys.exit()

# https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}

data = response.json()

current = data["currentConditions"]

city = data["address"]
temperature = current["temp"]
condition = current["conditions"]
humidity = current["humidity"]


print(city)
print(temperature)
print(condition)
print(humidity)

