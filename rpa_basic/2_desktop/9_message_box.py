import pyautogui
# pyautogui.countdown(3)
# print('자동화 시작')

# pyautogui.alert('자동화 수행에 실패 했습니다.','경고') # 확인 버튼만 있는 팝업
# result = pyautogui.confirm('계속 ㄱ?','확인')
# print(result)
result = pyautogui.prompt('파일명을 무엇으로?','입력') # 사용자 입력
print(result)
result = pyautogui.password('암호 입력')