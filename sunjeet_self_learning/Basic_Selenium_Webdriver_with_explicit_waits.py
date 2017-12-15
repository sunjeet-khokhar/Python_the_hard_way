from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# 2. Lets now redo the solution and this time use explicit wait
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.trademe.co.nz")
login_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'LoginLink')))
login_button.click()
email_id = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'page_email')))
email_id.send_keys('sunjeet81@gmail.com')
password = driver.find_element_by_id('page_password')
password.send_keys('yorks64')
login_button = driver.find_element_by_id('LoginPageButton')
login_button.click()
#user_name_after_login=driver.find_element_by_id('//*[@id="container"]/div[1]/div[1]/div[2]/div/p')
#user_name_after_login_located = WebDriverWait(driver,10).until(EC.presence_of_element_located(user_name_after_login))
try:
    user_name_after_login_located = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[1]/div[2]/div/p')))
except NoSuchElementException:
    print('Oops, Test failed, Element not located')
finally:
    driver.quit()
    
 
    
    
  
