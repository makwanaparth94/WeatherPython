from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from WeatherUI.data import data

class UIOps:
    def __init__(self):
        self.driver = None

    def get_driver(self):
        if data.browser == "chrome":
            self.driver = webdriver.Chrome(data.chrome_binary_path)
        elif data.browser == "firefox":
            self.driver = webdriver.Chrome(data.firefox_binary_path)
        return self.driver

    def open_browser(self):
        driver = self.get_driver()
        driver.get(data.url)
        driver.maximize_window()
        driver.implicitly_wait(data.wait)


    def click_element_by_xpath(self, element_path):
        driver = self.get_driver()
        element = driver.find_element_by_xpath(element_path).click()
        return element

    def click_element_by_ID(self, element_path):
        driver = self.get_driver()
        element = driver.find_element_by_id(element_path).click()
        return element

    def click_element(self, locator, element_path):
        driver = self.get_driver()
        element = driver.find_element(locator, element_path).click()
        return element

    def get_element_text(self, locator, element_path):
        driver = self.get_driver()
        element_text = driver.find_element(locator, element_path).text()
        return element_text

    def explicit_wait_and_moveto_alert(self):
        driver = self.get_driver()
        WebDriverWait(driver, data.alert_wait).until(cond.alert_is_present())
        alert_obj = driver.switch_to.alert
        return alert_obj

    def isAlreadySelected_by_ID(self, element_path):
        driver = self.get_driver()
        element = driver.find_element_by_id(element_path)
        if element.is_selected():
            return True
        else:
            return False

    def close_browser(self):
        driver = self.get_driver()
        driver.quit()





