from WeatherUI.data import data
from WeatherUI.ui_operations import UIOps
import pytest


@pytest.fixture(scope="module")
def set_up():
    UIOps().open_browser()
    yield
    UIOps().close_browser()


class UIimpl:

    def cancel_alert(self):
        UIOps().explicit_wait_and_moveto_alert().dismiss()

    def get_weather_info_by_selecting_city(self):

        UIOps().click_element_by_xpath(data.openExtraMenuBars_xpath)  # Expand the menu bar
        UIOps().click_element_by_xpath(data.weatherTab_XPATH) # Click on Weather tab
        #select a city
        if (UIOps().isAlreadySelected_by_ID(data.city)):
            UIOps().click_element(data.locator, data.city_text)
        else:
            UIOps().click_element(data.locator, data.city)
            UIOps().click_element(data.locator, data.city_text)
        city_temp_in_celcius = UIOps().get_element_text(data.locator, data.tempForSelecetedCity)
        print("city_temp_in_celcius:::",city_temp_in_celcius)







