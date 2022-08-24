from flightweather import FlightAPI, WeatherAPI
import logging
import json
from time import sleep
import pandas as pd

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    secrets_path = "secrets/credentials.json"

    with open(secrets_path, "rt") as f:
        creds = json.load(f)
        api_key = creds["OpenWeatherAPI"]

    lat_lon = {
        "lat": 50.1213479,
        "lon": 8.4964818
    }

    weather = WeatherAPI(api_key, **lat_lon)
    flights = FlightAPI(creds["airlabsAPI"])
    flights.params["airline_icao"] = "DLH"
    flights.params["flight_iata"] = "LH492"


    while True:
        data = flights.get()
        drop_cols = "flight_number flight_icao flight_iata dep_icao dep_iata arr_icao arr_iata airline_icao airline_iata aircraft_icao".split(" ")
        data.drop(columns=drop_cols, inplace=True)
        weather.params["lon"] = data.lng
        weather.params["lat"] = data.lat
        weather_data = weather.get()
        data = pd.concat([data, weather_data], axis="columns")
        print(data)
        sleep(10)
