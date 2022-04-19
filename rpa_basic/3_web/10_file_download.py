from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# 파일 다운로드 경로 지정
chrome_options = Options()
chrome_options.add_experimental_option('prefs', {'download.default_directory': r'C:\Users\dnwnd\OneDrive\바탕 화면\PythonWorkspace'})

browser = webdriver.Chrome(options=chrome_options)
browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('/html/body/p[2]/a')
elem.click()

time.sleep(5)
browser.quit()