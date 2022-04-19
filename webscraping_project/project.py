import re
from attr import attr
import requests
from bs4 import BeautifulSoup

def create_soup(url):
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
    res = requests.get(url,headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,'lxml')
    return soup

def print_news(index, title, link):
    print('{}. {}'.format(index+1, title))
    print(' (링크: {})'.format(link))

def scrape_weather():
    print('[오늘의 날씨]')
    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%8B%9C%ED%9D%A5+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hP%2FGYdprvN8ssFZzsmGssssssM0-366507'
    soup = create_soup(url)
    
    cast = soup.find('p', attrs={'class':'summary'}).get_text()

    curr_temp = soup.find('div',attrs={'class':'temperature_text'}).get_text().strip()
    min_temp = soup.find('span',attrs={'class':'lowest'}).get_text()
    max_temp = soup.find('span',attrs={'class':'highest'}).get_text()

    morning_rain_rate = soup.find('span',attrs={'class':'rainfall'}).get_text()
    evening_rain_rate = soup.find('span',attrs={'class':'rainfall'}).get_text()

    pm10 = soup.find('li',attrs={'class':'item_today level1'}).get_text().strip()
    pm25 = soup.find('li',attrs={'class':'item_today level3'}).get_text().strip()

    print(cast)
    print('{} ({}/ {})'.format(curr_temp,min_temp,max_temp))
    print('오전강수 확률 {} / 오후강수 확률 {}'.format(morning_rain_rate,evening_rain_rate))
    print('{}, {}'.format(pm10, pm25))
    print()


def scrape_headline_news():
    print('[헤드라인 뉴스]')
    url = 'https://news.naver.com/main/main.naver?mode=LSD&mid=shm&sid1=100'
    soup = create_soup(url)
    news_list = soup.find('ul', attrs={'class':'cluster_list'}).find_all('li', limit= 3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find('img')
        if img:
            a_idx = 1

        title = news.find_all('a')[a_idx].get_text()
        link = news.find_all('a')[a_idx]['href']
        print_news(index, title, link)
    print()

def scrape_it_news():
    print('[IT 뉴스]')
    url = 'https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230'
    soup = create_soup(url)
    news_list = soup.find('ul',attrs={'class':'type06_headline'}).find_all('li', limit=3)
    for index, news in enumerate(news_list):
        a_idx = 0
        img = news.find('img')
        if img:
            a_idx = 1 # img태그가 있으면 1번째 img태그의 정보를 사용

        title = news.find_all('a')[a_idx].get_text().strip()
        link = news.find_all('a')[a_idx]['href']
        print_news(index,title,link)
    print()

def scrape_english():
    print('[오늘의 영어 회화]')
    url = 'https://www.hackers.co.kr/?c=s_eng/eng_contents/I_others_english&keywd=haceng_submain_gnb_eng_I_others_english&logger_kw=haceng_submain_gnb_eng_I_others_english'
    soup = create_soup(url)
    sentences = soup.find_all('div', attrs={'id':re.compile('^conv_kor_t')})
    print('(영어 지문)')
    for sentence in sentences[len(sentences)//2:]:
        print(sentence.get_text().strip())
    print()
    print('(한글 지문)')
    for sentence in sentences[:len(sentences)//2]:
        print(sentence.get_text().strip())
    print()

if __name__ == '__main__':
    scrape_weather() # 오늘의 날씨 정보 가져오기
    scrape_headline_news()
    scrape_it_news()
    scrape_english()