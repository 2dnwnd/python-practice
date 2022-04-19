import pyautogui

# fw = pyautogui.getActiveWindow() # 현재 활성화된 창
# print(fw.title) # 창의 제목
# print(fw.size) # 창의 크기
# print(fw.left, fw.top, fw.right, fw.bottom) # 창의 좌표 정보

# for w in pyautogui.getAllWindows():
#     print(w)

w = pyautogui.getWindowsWithTitle('제목 없음')[0]

print(w)
if w.isActive == False:
    w.activate()