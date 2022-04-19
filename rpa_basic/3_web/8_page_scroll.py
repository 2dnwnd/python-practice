import time
from selenium import webdriver

browser = webdriver.Chrome()
browser.get('https://shopping.naver.com/home/p/index.naver')

# 검색창에 무선마우스 입력
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys('무선마우스')

# 검색버튼 클릭
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤
# browser.execute_script('window.scrollTo(0,1080)')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

interval = 2

# 현재 문서 높이를 가져와서 저장
pre_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    time.sleep(interval)

    curr_height = browser.execute_script('return document.body.scrollHeight')
    if curr_height == pre_height: #직전 높이와같으면, 높이변화가 없으면
        break
    
    pre_height = curr_height

# 맨위로 올리기
browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)
browser.quit()