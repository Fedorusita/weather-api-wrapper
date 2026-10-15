from fastapi import FastAPI
from typing import Literal
from pydantic import BaseModel
from weather_service import get_weather

app = FastAPI()

class WeatherResponse(BaseModel):
    city: str
    temperature: float
    unit: Literal["celsius", "fahrenheit"]
    condition: str

@app.get("/")
async def read_item():
    return{"message": "Welcome to Weather API"}

@app.get("/weather/{city}", response_model=WeatherResponse)
def read_city(city: str, unit: Literal["celsius", "fahrenheit"] = "celsius"):
    weather = get_weather(city)
    temperature = weather["temperature"]
    condition = weather["condition"]
    if unit == "fahrenheit":
        temperature = temperature * (9 / 5) + 32
    
    return{
            "city": city,
            "temperature": temperature,
            "unit": unit,
            "condition": condition
        }

