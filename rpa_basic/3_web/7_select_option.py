import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_option')

browser.switch_to.frame('iframeResult')

# elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
# elem.click()

# 텍스트 값을 통해서 선택하는 방법
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
elem.click()

elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')

time.sleep(5)

browser.quit()