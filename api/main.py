from typing import List, Optional

import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ForecastRequest(BaseModel):
    latitude: float
    longitude: float
    elevation: Optional[float] = None
    hourly: Optional[List[str]] = None
    daily: Optional[List[str]] = None
    current_weather: Optional[bool] = False
    temperature_unit: Optional[str] = "celsius"
    windspeed_unit: Optional[str] = "kmh"
    precipitation_unit: Optional[str] = "mm"
    timeformat: Optional[str] = "iso8601"
    timezone: Optional[str] = "GMT"
    past_days: Optional[int] = 0
    forecast_days: Optional[int] = 7
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    models: Optional[List[str]] = None
    cell_selection: Optional[str] = "land"


class ArchiveRequest(BaseModel):
    latitude: float
    longitude: float
    start_date: str
    end_date: str
    elevation: Optional[float] = None
    hourly: Optional[List[str]] = None
    daily: Optional[List[str]] = None
    temperature_unit: Optional[str] = "celsius"
    windspeed_unit: Optional[str] = "kmh"
    precipitation_unit: Optional[str] = "mm"
    timeformat: Optional[str] = "iso8601"
    timezone: Optional[str] = "GMT"
    cell_selection: Optional[str] = "land"


@app.post("/v1/forecast")
async def forecast(request: ForecastRequest):
    # Prepare the parameters for the API request
    params = request.dict()
    print(params)
    if request.hourly:
        params["hourly"] = ",".join(request.hourly)
    if request.daily:
        params["daily"] = ",".join(request.daily)
    if request.models:
        params["models"] = ",".join(request.models)

    # Make the API call
    response = requests.get("https://api.open-meteo.com/v1/forecast", params=params)

    # Validate and return the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": True, "message": "Cannot fetch data from Open-Meteo API"}


@app.post("/v1/archive")
async def archive(request: ArchiveRequest):
    # Prepare the parameters for the API request
    params = request.dict()
    if request.hourly:
        params["hourly"] = ",".join(request.hourly)
    if request.daily:
        params["daily"] = ",".join(request.daily)

    # Make the API call to the Open-Meteo Archive endpoint
    response = requests.get("https://api.open-meteo.com/v1/archive", params=params)

    # Validate and return the response
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": True, "message": "Cannot fetch data from Open-Meteo API"}
