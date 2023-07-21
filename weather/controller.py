from datetime import datetime
from .models import Weather
import requests
from ..utils import constants


class WeatherController:
    @staticmethod
    def get_weather(lat, lon):
        url = constants.WEATHER_API_URL.format(
            lat, lon, constants.WEATHER_API_KEY)

        response = requests.get(url.format(lat, lon)).json()
        print(response['cod'])

        if response['cod'] != constants.CODE_OK:
            return response

        temperature = response['main']['temp']
        name = response['name']
        time = datetime.now()
        res = Weather.add_wather(lat, lon, temperature, name, time)
        return response

    @staticmethod
    def show_weather():
        res = Weather.show_all()
        return res
