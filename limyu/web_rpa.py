from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys, os,  time

# Start Google Chrome
if getattr(sys, 'frozen', False):
    driver_path = os.path.join(sys._MEIPASS, "chromedriver.exe")
    driver = webdriver.Chrome(driver_path)
else:
    driver = webdriver.Chrome()

# Open Google.com
driver.get('https://www.google.com/')


search_input = driver.find_element_by_xpath('//input[@title="검색"]')
search_input.send_keys("RAP")


search_input.send_keys(Keys.ENTER)
