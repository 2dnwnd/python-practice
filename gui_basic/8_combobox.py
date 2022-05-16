import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('GUI')
root.geometry('480x320') # 가로 * 세로 

values = [str(i) + '일' for i in range(1, 32)] # 1일부터 31일까지
combobox = ttk.Combobox(root, height=5, values=values) # state에 readonly값을 적용하면
combobox.pack()
combobox.set('카드 결제일') # 최초 목록 제목 설정

def btncmd():
    print(combobox.get())

btn = Button(root, text='주문', command=btncmd)
btn.pack()

root.mainloop()
