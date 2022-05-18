import keyboard
import time
from PIL import ImageGrab

def screenshot():
    curr_time = time.strftime("_%Y%m%d_%H%M%S")
    img = ImageGrab.grab()
    img.save('image{}.png'.format(curr_time)) # ex_ image_2022

keyboard.add_hotkey('F9', screenshot)   # F9를 누르면 스크린샷 저장

keyboard.wait('esc') # esc를 누를때까지 프로그램 수행