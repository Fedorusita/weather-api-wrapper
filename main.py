from fastapi import FastAPI
from typing import Literal
from pydantic import BaseModel

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
async def read_city(city: str, unit: Literal["celsius", "fahrenheit"] = "celsius"):
    temperature = 20
    if unit == "fahrenheit":
        temperature = temperature * (9 / 5) + 32
    
    return{
            "city": city,
            "temperature": temperature,
            "unit": unit,
            "condition": "Sunny"
        }
    