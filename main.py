from fastapi import FastAPI
from typing import Literal

app = FastAPI()

@app.get("/")
async def read_item():
    return{"message": "Welcome to Weather API"}

@app.get("/weather/{city}")
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
    