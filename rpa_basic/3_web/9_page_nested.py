import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()
browser.get('https://www.w3schools.com/html/')

time.sleep(5)

elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# # ActionChain
# actions = ActionChains(browser)
# actions.move_to_element(elem).perform()

# 방법 2: 좌표 정보 이용
xy = elem.location_once_scrolled_into_view #함수가 아님
print('type :', type(xy))
print('value :', xy)

elem.click()

time.sleep(5)
browser.quit()