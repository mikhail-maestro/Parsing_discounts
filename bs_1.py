from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

url = 'https://tl.ashahov.ru/samoocenka'
ua = UserAgent()
fake_ua = {'user-agent': ua.random}


response = requests.get(url, headers=fake_ua)

response.encoding = 'utf-8'

soup = BeautifulSoup(response.text, 'lxml')
#print(soup)
div = soup.find('div', {'field':'tn_text_1630517417361'}).text
#for d in div:
#    print(d)
print(div)
