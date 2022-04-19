import pyautogui

# 마우스 이동 (절대좌표)
# pyautogui.moveTo(100, 100) # 지정한 위치로 마우스를 이동
# pyautogui.moveTo(100, 200, duration=5) # 5초동안 위치로 이동ㄴㅁ

# pyautogui.moveTo(100,100)
# pyautogui.moveTo(200,200)
# pyautogui.moveTo(300,300)

# 현재커서가 있는 위치부터 움직임(상대좌표)
pyautogui.move(100,100)

p = pyautogui.position()
print(p[0],p[1])
print(p.x,p.y)