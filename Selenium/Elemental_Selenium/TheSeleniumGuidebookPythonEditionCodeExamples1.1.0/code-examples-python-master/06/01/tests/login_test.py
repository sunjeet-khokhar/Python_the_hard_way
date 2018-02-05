import pytest
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin():

    @pytest.fixture
    def driver_initialize(self, request):
        driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_


    def test_valid_credentials(self, driver_initialize):
        driver_initialize.get("http://the-internet.herokuapp.com/login")
        #driver.find_element(By.ID, "username").send_keys("tomsmith")
        #driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        #driver.find_element(By.CSS_SELECTOR, "button").click()
