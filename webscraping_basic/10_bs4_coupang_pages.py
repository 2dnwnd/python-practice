import requests
import re
from bs4 import BeautifulSoup

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

for i in range(1,6):
    print('페이지',i)
    url = 'https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor='.format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'lxml')

    items = soup.find_all('li', attrs={'class':re.compile('^search-product')})
    for item in items:
        total = len(items)

        # 광고 제품은 제외
        ad_badge = item.find('span',attrs={'class':'ad-badge-text'})
        if ad_badge:
            # print(' 광고상품 제외 합니다.')
            total -= 1
            continue

        # 애플 제품은 제외
        name = item.find('div',attrs={'class':'name'}).get_text() # 제품명
        if 'Apple' in name:
            # print(' 애플 상품 제외합니다')
            total -= 1
            continue

        price = item.find('strong', attrs={'class':'price-value'}).get_text() # 가격
        
        # 리뷰 50개 이상, 평점 4.5 이상되는 것만 조회
        rate = item.find('em', attrs={'class':'rating'}) # 평정
        #(평점없는 상품 있어서)
        if rate:
            rate = rate.get_text()
        else:
            # print('평점 없는 상품 제외')
            total -= 1
            continue
        rate_cnt = item.find('span', attrs={'class':'rating-total-count'}) # 평점수
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()[1:-1]
        else:
            # print('평점 수 없는 상품 제외')
            total -= 1
            continue

        link = item.find('a',attrs={'class':'search-product-link'})['href']

        if float(rate) >=4.5 and int(rate_cnt) >= 50:
            # print(name, price, rate, rate_cnt)
            print(f'제품평 : {name}')
            print(f'가격 : {price}')
            print(f'평점 : {rate}점 ({rate_cnt}개)')
            print('바로가기 : {}'.format('https://www.coupang.com' +link))
            print('-'*20)
print('총 개수는',total)