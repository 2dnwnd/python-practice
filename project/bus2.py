import time
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

user_id = 'dnwnd1019'
user_pw = 'aa1216137'

browser = webdriver.Chrome()
browser.get('https://map.naver.com/v5/bus/bus-route')
time.sleep(3)

elem = browser.find_element(By.XPATH, '//*[@id="container"]/shrinkable-layout/div/bus-home/div[1]/bus-search/div/div/div/div/div/div')
elem.send_keys('31-7')
elem.send_keys(Keys.ENTER)