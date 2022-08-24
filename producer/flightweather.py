import requests
import json
import logging
import pandas as pd

class RestAPI:
    def __init__():
        pass

    def call(self, *args):
        response = requests.get(url=self._endpoint_url, params=self.params)
        self.data = response.json()

class WeatherAPI(RestAPI):
    """
    Wrapper for OpenWeather API
    """
    def __init__(self, api_key, lat, lon):
        self._endpoint_url="https://api.openweathermap.org/data/2.5/weather?"
        self.params = {
            "appid": api_key,
            "lat": lat,
            "lon": lon,
            "units": "metric"
        }

    def get(self, metric="main"):
        self.call()
        data = self.data[metric]
        logging.info(data)
        df = pd.DataFrame([data])
        return df

class FlightAPI(RestAPI):
    """
    Wrapper for AirLabs API
    """
    def __init__(self, api_key, endpoint="flights"):
        self._endpoint_url=f"https://airlabs.co/api/v9/{endpoint}?"
        self.params = {
            "api_key": api_key
        }

    def get(self):
        self.call()
        logging.debug(self.data)
        data = self.data["response"]
        logging.debug(data)
        if type(data) != list:
            data = [data]
        df = pd.DataFrame(data)
        return df