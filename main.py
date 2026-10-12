from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_item():
    return{"message": "Welcome to Weather API"}

@app.get("/weather/{city}")
async def read_city(city: str):
    return{
            "city": city,
            "temperature": 20,
            "condition": "Sunny"
        }