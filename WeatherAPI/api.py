import requests
from WeatherAPI.data import data

class API:

    def get_weatherinfo_by_cityname(self):
        response = requests.get(data.url + data.cityname + data.api_key)
        return response

