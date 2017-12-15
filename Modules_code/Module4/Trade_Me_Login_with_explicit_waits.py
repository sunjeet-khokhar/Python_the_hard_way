from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# 2. Lets now redo the solution and this time use explicit wait
class TradeMe_Login:
               
 def login_test(self):
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
  try:
   user_name_after_login_located = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="container"]/div[1]/div[1]/div[2]/div/p')))
  except (NoSuchElementException,TimeoutException) as e:
   print('Oops, Test failed, user name element not located')
   driver.quit()  
  
 def logout_test(self):
  logout_link = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/p/a')
  logout_link.click()
  try:
   login_link = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.ID,'LoginLink1')))
  except (NoSuchElementException,TimeoutException) as e:
   print('Oops , Test failed login link could not be found')
   driver.quit()
 
 def teardown(self):
  driver.quit()
  
   
test = TradeMe_Login()
test.login_test()
test.logout_test()
test.teardown()





    
 
    
    
  
