import pytest
import json
from WeatherAPI.api import API


class TestAPI:
    def test_get_current_weather_for_city(self):
        response = API.get_weatherinfo_by_cityname(self)
        rs = response.json()
        print(rs["main"]["temp"])



