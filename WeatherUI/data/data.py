from selenium.webdriver.common.by import By

url = "https://www.ndtv.com/"
browser = "chrome"
chrome_binary_path = r"D:\shivi python\WeatherPython\WeatherUI\executable\chromedriver.exe"
firefox_binary_path = ""

#######################		LOCATOR DATA	#######################
#Home Page
cancelAlert_xpath = '//*[@id="__cricketsubscribe"]/div[2]/div[2]/a[1]'
openExtraMenuBars_xpath = '//*[@id="h_sub_menu"]'
weatherTab_XPATH = '//*[@id=\\"subnav\\"]/div/div/div/div/div/a[8]'

#Weather Page
city = 'Mumbai'
#validateTextOnWeatherPage = 'div.infoHolder'
#hoverOnSelectedCity = "//*[contains(@title,'Mumbai')]"
city_text = "//div[contains(text(),'Mumbai')]"
locator = By.XPATH
tempForSelecetedCity = "//*[contains(text(),'Temp in Degrees')]"
humidityForSelectedCity = '//div[@class="leaflet-popup-content"]/div/span[3]'

#######################		TEST DATA	#######################
wait = 5
alert_wait = 30
#Validator range must contain INT numbers only
setup_TempDiffInCelsius = 0
setup_HumidityDiffInPercentage = 0