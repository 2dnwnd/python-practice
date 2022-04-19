import requests
from bs4 import BeautifulSoup

url = 'https://play.google.com/store/movies/top'
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"
            ,'Accept-Language':'ko-KR,ko'
        }

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'lxml')

movies = soup.find_all('div',attrs={'class':'ImZGtf mpg5gc'})
# print(len(movies))

# with open('movie.html','w',encoding='utf8') as f:
    # f.write(res.text)
    # f.write(soup.prettify()) # html파일을 정돈되게
 