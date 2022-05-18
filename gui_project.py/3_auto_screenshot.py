import time
from PIL import ImageGrab

time.sleep(5)

for i in range(10):
    img = ImageGrab.grab() # 현재 스크린의 이미지를 가져옴
    img.save('imge{}.png'.format(i+1)) # 파일로 저장
    time.sleep(2) 