import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://shopping.naver.com/home/p/index.naver')

# 가는날

time.sleep(5)
browser.quit()