import requests
from bs4 import BeautifulSoup

url = 'https://comic.naver.com/webtoon/weekday'
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, 'lxml')
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # soup 객체에서 처음 발견되는 a element 출력
# print(soup.a.attrs) # a element의 속성정보를 출력
# print(soup.a['href']) # a element의 href 속성 값 출력

# print(soup.find('a', attrs={'class':'Nbtn_upload'}))

# print(soup.find('li', attrs={'class':'rank01'}))
# rank1 = soup.find('li', attrs={'class':'rank01'})
# print(rank1.a.get_text())
# rank2 =  rank1.next_sibling.next_sibling
# rank2 = rank1.find_next_sibling('li')
# print(rank1.find_next_siblings('li'))

webtoon = soup.find('a',text='외모지상주의-375화 일해회 (2계열사) [04]')