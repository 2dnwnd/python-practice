# print(5)
# print(5>10)

# name ='해피'
# age = 4
# print(name,'는',age,'살 입니다.')
# print(name + '는 ' + str(age) + '살 입니다.')

# station = '사당'
# print(station+'행 열차가 들어오고 있습니다.')
# station = '신도림'
# print(station+'행 열차가 들어오고 있습니다.')
# station = '인천공항'
# print(station+'행 열차가 들어오고 있습니다.')

# print(abs(-4))
# print(pow(4,2))
# print(max(1,10))
# print(round(3.14))

# from math import *
# print(floor(4.66))
# print(ceil(4.66))
# print(sqrt(16))

# from random import *

# day = randint(4,29)
# print('오프라인 스터디 모임 날짜는 매월 '+str(day)+'일로 결정됨')

# jumin = "990120-1234567"
# print(jumin[-7::-1])

# print('나는 %d살입니다.' % 25) #정수
# print('나는 %s을 좋아해요' % '파이썬') #문자열
# print('Apple은 %c로 시작해요' % 'A') #문자
# print('나는 %s색과 %s색을 좋아해요' % ('빨간', '파란'))

# print('나는 {}색과 {}색을 좋아해요'.format('빨간','파란'))

# site = 'http://youtube.com'
# a = site.replace('http://', '')
# b = a.find('.')
# new_site = a[0:b]
# word_len = len(new_site)
# word_e = new_site.count('e')

# password = new_site[0:3]+str(word_len)+ str(word_e) + '!'
# print('%s사이트의 비밀번호는 %s입니다.' % (site,password))
# print('{}사이트의 비밀번호는 {}입니다.'.format(site,password))


# from random import *
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# shuffle(lst)
# chicken = sample(lst,1)
# shuffle(lst)
# coffee = sample(lst,3)
# print('-- 당첨자 발표 --')
# print('치킨 당첨자 :', chicken)
# print('커피 당첨자 :', coffee)
# print(' -- 축하합니다 --')


# absent = [ 2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     elif student in no_book:
#         print('책을 안가져와? 죽어')
#         break
#     print('{}, 책을 읽어줘'.format(student))


# from random import *
# passenger = 0
# for i in range(1,51):
#     time = randint(5,51)
#     print('{}번째 손님 (소요시간 : {}분)'.format(i,time))
#     if 5<= time <= 15:
#         passenger += 1
# print('총 탑승 승객 :',passenger,'분')


# def std_weight(height, gender):
#     if gender == '남자':
#         weight = height * height * 22
#     else:
#         weight = height * height * 21
#     return round(weight,2)

# print(std_weight(1.78,'남자'))

# score_file = open('score.txt','w',encoding='utf8') #덮어쓰기
# print('수학 : 0',file=score_file)
# print('영어 : 50',file=score_file)
# score_file.close()

# score_file = open('score.txt','a',encoding='utf8') #이어쓰기
# print('과학 : 80',file=score_file)
# print('코딩 : 100',file=score_file)
# score_file.close()

# import pickle
# profile_file = open('profile.pickle','wb')
# profile = {'이름':'이우중','나이':30,'취미':['축구','코딩']}
# print(profile)
# pickle.dump(profile, profile_file)
# profile_file.close()

# import pickle

# with open('profile.pickle','rb',) as profile_file:
#     print(pickle.load(profile_file))
    
# class House:
#     # 매물 초기화 : 위치, 건물 종류, 매물 종류, 가격, 준공년도
#     def __init__(self, location, house_type, deal_type, price, completion_year):
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year = completion_year

#     # 매물 정보 표시
#     def show_detail(self):
#         print('{} {} {} {} {}'.format(self.location, self.house_type, self.deal_type,
#             self.price, self.completion_year))

# apartment = House('강남','아파트','매매','10억','2010년')
# opice = House('마포','오피스텔','전세','5억','2007년')
# vila = House('송파','빌라','월세','500/50','2000년')

# houses = []
# houses.append(apartment)
# houses.append(opice)
# houses.append(vila)

# print('총 {}대의 매물이 있습니다.'.format(len(houses)))
# for house in houses:
#     house.show_detail()


# class SoldOutError(Exception):
#     pass

# chicken = 10 # 남은 치킨 수
# waiting = 1 # 홀 안에는 현재 만석. 대기번호 1부터 시작

# while(True):
#     try:
#         print("[남은 치킨 : {0}]".format(chicken))
#         order = int(input("치킨 몇 마리 주문하시겠습니까?"))
#         if order > chicken: # 남은 치킨보다 주문량이 많을 때
#             print("재료가 부족합니다.")
#         elif order <= 0:
#             raise ValueError
#         else:
#             print("[대기번호 {0}] {1} 마리 주문이 완료되었습니다.".format(waiting, order))
#             waiting += 1 # 대기번호 증가
#             chicken -= order # 주문 수 만큼 남은 치킨 감소

#         if chicken == 0:
#             raise SoldOutError

#     except ValueError:
#         print("잘못된 값을 입력하였습니다.")
#     except SoldOutError:
#         print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
#         break


# import theater_module
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.price_soldier(2)

# from travel import *
# # import travel.thailand
# # trip_tp = travel.thailand.ThailandPackage()
# # trip_tp.detail()

# import inspect
# import random

# from travel import thailand
# print(inspect.getfile(random))
# print(inspect.getfile(thailand))

#glob : 경로 내의 폴더/파일 목록 조회(원도우 dir)
# import glob
# print(glob.glob('*.py'))

# os : 운영체제에서 제공하는 기본기능
# import os
# print(os.getcwd()) #현재디렉토리 

# folder = 'sample_dir'

# if os.path.exists(folder):
#     print('이미 존재하는 폴더입니다.')
#     os.rmdir(folder)
#     print(folder,'폴더를 삭제하였습니다.')
# else:
#     os.makedirs(folder)
#     print(folder, '폴더를 생성하였습니다.')
# print(os.listdir())

# import time
# print(time.localtime())
# print(time.strftime('%Y-%m-%d %H:%M:%S'))

import byme
byme.sign()