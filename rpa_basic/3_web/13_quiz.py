import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('http://www.w3schools.com')
browser.maximize_window()

browser.find_element_by_xpath('//*[@id="main"]/div[2]/div/div[1]/a[1]').click()

browser.find_element_by_xpath('//*[@id="topnav"]/div/div/a[10]').click()

browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[text()="Contact Form"]').click()

first_name = '나도'
last_name = '코딩'
country = 'Canada'
subject = '퀴즈 완료하였습니다.'

browser.find_element_by_xpath('//*[@id="fname"]').send_keys(first_name)
browser.find_element_by_xpath('//*[@id="lname"]').send_keys(last_name)
browser.find_element_by_xpath('//*[@id="country"]/option[text()="{}"]'.format(country)).click()
browser.find_element_by_xpath('//*[@id="main"]/div[3]/textarea').send_keys(subject)

time.sleep(5)
browser.find_element_by_xpath('//*[@id="main"]/div[3]/a').click()

time.sleep(5)
browser.quit()