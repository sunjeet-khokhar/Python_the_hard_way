from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1.First part of the solution is without an explicit wait, prone to flakiness, poor test design

# create a new instance of webdriver for Chrome
driver = webdriver.Chrome()
#maximize browser window
driver.maximize_window()
# open the URL
driver.get("http://www.trademe.co.nz")
# baaaaaad design .... hard coded sleep time , just assumes that it will take less than 10 seconds to load the page
time.sleep(10)
# find the Login link
login_button = driver.find_element_by_id("LoginLink")
#click the button
login_button.click()
# baaaaaad design again , for the login page to load we have added another hard coded sleep
time.sleep(10)
#find and enter your email in the email id box
email_id = driver.find_element_by_id("page_email")
email_id.send_keys("sunjeet81@gmail.com")
#find and enter your password in the password box
password = driver.find_element_by_id("page_password")
password.send_keys("******")
# click login button
login_page_button = driver.find_element_by_id("LoginPageButton")
login_page_button.click()
#baaaaaad design again for adding hard coded sleep for the page to sync
time.sleep(15)
## here are looking for the xpath of the locator for the web element that displays the user name
try:
 user_name = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/p')
# throw an exception if the element is not found
except NoSuchElementException:
 print("Test failed, element not found ")
# quit the browser inspite of whatever happens , with the finally keyword
finally:
 driver.quit()
# another way to create a test condition is to use the inbuild assertion keyword --->
#user_name = driver.find_element_by_xpath('//*[@id="container"]/div[1]/div[1]/div[2]/div/p')
#assert user_name.is_displayed()
#print("Test passed")
 

 

 

    
    