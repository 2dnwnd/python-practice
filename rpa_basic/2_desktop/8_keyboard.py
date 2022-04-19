import pyautogui
w = pyautogui.getWindowsWithTitle('제목 없음')[0]
w.activate()

# pyautogui.write('12345')
# pyautogui.write('Nadocoding', interval=0.25)
# pyautogui.write('나도코딩')

# pyautogui.write(['t','e','s','t','left','left','right','1','a','enter'], interval=0.25)

# 특수 문자
# # shift 4 ->$
# pyautogui.keyDown('shift')
# pyautogui.press('4')
# pyautogui.keyUp('shift')

# # 조합키
# pyautogui.keyDown('ctrl')
# pyautogui.press('a')
# pyautogui.keyUp('ctrl')

# # 간편한 조합키
# pyautogui.hotkey('ctrl','a')

import pyperclip
# pyperclip.copy('나도코딩') # 클립보드에 복사
# pyautogui.hotkey('ctrl','v')

def my_write(text):
    pyperclip.copy(text)
    pyautogui.hotkey('ctrl','v')

my_write('우중')

# 자동화 프로그램 종료
# win : ctrl + alt + del