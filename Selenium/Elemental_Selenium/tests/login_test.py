import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Test_Login():
    

    @pytest.fixture
    def driver(self,request):
        driver_ = webdriver.Chrome()
        
        def quit():
            driver_.quit()
        
        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self,driver):
        driver.get('http://the-internet.herokuapp.com/login')
        driver.maximize_window()
        time.sleep(5)
        driver.find_element(By.ID,'username').send_keys('tomsmith')
        driver.find_element(By.ID,'password').send_keys('SuperSecretPassword!')
        driver.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
        time.sleep(5)
        assert driver.find_element(By.XPATH,'//*[@id="flash1"]').is_displayed()
        
        
