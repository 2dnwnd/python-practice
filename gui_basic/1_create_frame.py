from tkinter import *

root = Tk()
root.title('GUI')
# root.geometry('640x480+100+300') # 가로 * 세로 + x좌표 y좌표
root.geometry('640x480') # 가로 * 세로 

root.resizable(False, False) # x y값 변경불가 (창크기)

root.mainloop()