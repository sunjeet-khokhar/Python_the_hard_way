from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.select import Select


# for easy future changes and code maintainbility i have added all the locators and parameters like username/password at the top of the test
driver = webdriver.Chrome()
CONTINUE_BUTTON = (By.XPATH,'//*[@id="cms-search-panel-container"]/div/div/div/form/div[3]/div/button')
FLIGHT_CLASS_DROPDOWN = (By.ID,'serviceclass')
FLIGHT_CLASS_NAME = 'BUSINESS'
URL = 'https://www.airnewzealand.co.nz/home'

class AirNZ_search_flight:

    def search_flight(self):
        driver.maximize_window()
        driver.get(URL)
        continue_button = WebDriverWait(driver,10).until(EC.presence_of_element_located(CONTINUE_BUTTON))
        continue_button.click()
        flight_class_dropdown = WebDriverWait(driver,10).until(EC.presence_of_element_located(FLIGHT_CLASS_DROPDOWN))
        select = Select(flight_class_dropdown)
        select.select_by_value(FLIGHT_CLASS_NAME)

    def teardown(self):
        driver.quit()


test = AirNZ_search_flight()
test.search_flight()
test.teardown()










