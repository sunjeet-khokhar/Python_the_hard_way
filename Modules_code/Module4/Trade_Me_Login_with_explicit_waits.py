from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
LOGIN_BUTTON = (By.ID,'LoginLink')
EMAIL_ID = (By.ID,'page_email')
USER_NAME = <<enter use name>>
PASSWORD_LOCATOR = 'page_password'
USER_PASSWORD = <<enter password>>
LOGIN_BUTTON_on_LOGIN_PAGE = 'LoginPageButton'
USER_NAME_DISPLAY = (By.XPATH,'//*[@id="container"]/div[1]/div[1]/div[2]/div/p')
LOGOUT_XPATH = '//*[@id="container"]/div[1]/div[1]/div[2]/div/p/a'


# 2. Lets now redo the solution and this time use explicit wait
class TradeMe_Login:
               
 def login_test(self):
  driver.maximize_window()
  driver.get("http://www.trademe.co.nz")
  login_button = WebDriverWait(driver,10).until(EC.presence_of_element_located(LOGIN_BUTTON))
  login_button.click()
  email_id = WebDriverWait(driver,10).until(EC.presence_of_element_located(EMAIL_ID))
  email_id.send_keys(USER_NAME)
  password = driver.find_element_by_id(PASSWORD_LOCATOR)
  password.send_keys(USER_PASSWORD)
  login_button = driver.find_element_by_id(LOGIN_BUTTON_on_LOGIN_PAGE)
  login_button.click()
  try:
   user_name_after_login_located = WebDriverWait(driver,10).until(EC.presence_of_element_located(USER_NAME_DISPLAY))
  except (NoSuchElementException,TimeoutException) as e:
   print('Oops, Test failed, user name element not located')
   driver.quit()  
  
 def logout_test(self):
  logout_link = driver.find_element_by_xpath(LOGOUT_XPATH)
  logout_link.click()
  try:
   login_link = WebDriverWait(driver,10).until(EC.presence_of_element_located(LOGIN_BUTTON))
  except (NoSuchElementException,TimeoutException) as e:
   print('Oops , Test failed login link could not be found')
   driver.quit()
 
 def teardown(self):
  driver.quit()
  
   
test = TradeMe_Login()
test.login_test()
test.logout_test()
test.teardown()





    
 
    
    
  
