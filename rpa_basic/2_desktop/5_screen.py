import pyautogui

# 스크린샷 찍기
img = pyautogui.screenshot()
img.save('hello.png')

pixel = pyautogui.pixel(28,18)
print(pyautogui.pixelMatchesColor(28,18,pixel))