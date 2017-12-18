from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# for easy future changes and code maintainbility i have added all the locators and parameters  at the top of the test , so they are all in one place 
driver = webdriver.Chrome()
VIEW_ALL_ONE_DOLLAR_AUCTIONS = (By.XPATH,'//*[@id="OneDollarReserveStripe"]/div/div[1]/span[2]/a/span')
LIST_OF_AUCTIONS = (By.ID,'ListViewList')

class TradeMe_Scraping:

    def scrape_one_dollar_auctions(self):
        driver.maximize_window()
        driver.get("http://www.trademe.co.nz")
        #explicitly wait for prescence of the "view all" link to apear locator !
        view_all_one_dollar_auctions = WebDriverWait(driver,10).until(EC.presence_of_element_located(VIEW_ALL_ONE_DOLLAR_AUCTIONS))
        # click on the "view_all" hyperlink
        view_all_one_dollar_auctions.click()
        # on this page wait explicit for the element LIST_OF_AUCTIONS
        auction_items_list = WebDriverWait(driver,10).until(EC.presence_of_element_located(LIST_OF_AUCTIONS))
        #  https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions 
        # This technique is called list comprehension , a neat way to populate a list with all elements that have the tag name "img" i.e. are an image element under "auction_items_list"
        all_auction_images = [x for x in auction_items_list.find_elements_by_tag_name('img')]
        # iterate through each image and get the alt text property 
        for img in all_auction_images:
            auction_heading = img.get_property('alt')
            # print the alt text property 
            print(auction_heading)
        # close the browser    
        driver.quit()

test = TradeMe_Scraping()
test.scrape_one_dollar_auctions()










