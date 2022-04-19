from turtle import width
import pyautogui

file_menu = pyautogui.locateOnScreen('file_menu.png')
print(file_menu)
pyautogui.click(file_menu)

# 속도 개선
# 1. GrayScale
file_menu = pyautogui.locateOnScreen('file_menu.png', grayscale = True)
pyautogui.moveTo

# 2. 범위 지정
# file_menu = pyautogui.locateOnScreen('file_menu.png', region=(x,y, width,height))
pyautogui.moveTo

# 3. 정확도 조정 (정확도 떨어트리기)
file_menu = pyautogui.locateOnScreen('file_menu.png',confidence=0.9)
pyautogui.moveTo

# 자동화 대상이 바로 보여지지 않는 경우
# 1. 계속 기다리기
while file_menu is None:
    file_menu = pyautogui.locateOnScreen('file_menu.png')
    print('발견실패')
pyautogui.click(file_menu)

# 2. 일정시간동안 기다리기
import time
import sys

timeout = 10 # 10초대기
start = time.time() # 시작시간 설정
file_menu = None
while file_menu is None:
    file_menu = pyautogui.locateOnScreen('file_menu.png')
    end = time.time()
    if end - start > timeout: #지정한 10초를 초과하면
        print('시간 종료')
        sys.exit()

def find_target(img_file, timeout = 30):
    start = time.time()
    target = None
    while target is None:
        target = pyautogui.locateOnScreen(img_file)
        end = time.time()
        if end - start > timeout: 
            break
    return target

def my_click(img_file, timeout=30):
    target = find_target(img_file,timeout)
    if target:
        pyautogui.click(target)
    else:
        print(f'[Timeout {timeout}s] Target not found ({img_file}). Terminate program.')
        sys.exit


my_click('file_menu.png', 10)