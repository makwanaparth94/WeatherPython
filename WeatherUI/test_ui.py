import pytest
from WeatherUI.ui_impl import *


@pytest.mark.usefixtures('set_up')
class TestUI:

    def test_display_of_weather_details_on_city_selection(self):
        #UIimpl().cancel_alert()
        UIimpl().get_weather_info_by_selecting_city()

