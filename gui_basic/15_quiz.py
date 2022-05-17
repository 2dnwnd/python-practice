import os
from tkinter import *

root = Tk()
root.title('제목 없음 - Windows 메모장')
root.geometry('640x480') # 가로 * 세로 

# 스크롤바
scrollbar = Scrollbar(root)
scrollbar.pack(side='right', fill='y')


# 본문
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(side='left', fill='both', expand=True) # 화면 꽉채우기
# txt.insert(END, '글자를 입력하세요')
scrollbar.config(command=txt.yview)

# 열기,저장 파일이름
filename = 'mynote.txt'

def open_file():
    if os.path.isfile(filename): # 파일이 있스면 트루
        with open(filename, 'r', encoding='utf8') as file:
            txt.delete('1.0', END) # 텍스트 본문 삭제하고
            txt.insert(END, file.read()) # 내용 입력하기

def save_file():
    with open(filename, 'w', encoding='utf8') as file:
        file.write(txt.get('1.0', END))


# 메뉴
menu = Menu(root)

# 파일 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='열기', command=open_file)
menu_file.add_command(label='저장', command=save_file)
menu_file.add_separator()
menu_file.add_command(label='끝내기', command=root.quit)
menu.add_cascade(label='파일', menu=menu_file)

# 나머지 메뉴
menu.add_cascade(label='편집')
menu.add_cascade(label='서식')
menu.add_cascade(label='보기')
menu.add_cascade(label='도움말')


root.config(menu=menu)
root.mainloop()