# 파일 기본
import os
# os.chdir('rpa_basic')
# print(os.getcwd()) # current working directory 현재 작업 공간
# os.chdir('..') # 부모폴더로 이동
# print(os.getcwd()) 

# 파일 경로 만들기

# os.path.join(os.getcwd(), 'my_file.txt')

# # 파일 경로에서 폴더 정보 가져오기
# os.path.dirname(r'C:\Users\dnwnd\OneDrive\바탕 화면\PythonWorkspace')

# # 파일 정보 가져오기
# import time
# import datetime

# #파일의 생성 날짜
# ctime = os.path.getctime('hello.png')
# print(ctime)
# print(datetime.datetime.fromtimestamp(ctime))

# # 파일 수정날짜
# mtime = os.path.getmtime('hello.png')
# print(datetime.datetime.fromtimestamp(mtime))

# # 파일 마지막 접근 날짜
# atime = os.path.getatime('hello.png')
# print(datetime.datetime.fromtimestamp(atime))

# # 파일 크기
# size = os.path.getsize('hello.png')
# print(size) #바이트 단위

# 파일 목록 가져오기
# print(os.listdir())
# print(os.listdir('rpa_basic'))
# result = os.walk('rpa_basic')

# for root, dirs, files in result:
#     print(root, dirs, files)

# 파일 만들기
# open('new_file.txt','a').close()