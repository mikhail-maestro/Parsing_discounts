from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import requests
import math

# ghbdtn!!!!

ua = UserAgent()
headers = {
    'user-agent': ua.random,
    #'x-requested-with':'XMLHttpRequest'
}


url = 'https://lenta.com/api/v1/nodes/nodeinfo?nodeCode=gd6dd9b5e854cf23f28aa622863dd6913&searchPhrase=&pageId=cc4fe51d-b4c0-4c96-be9b-ffebb9d67753&storeId=&brandName=&filtersWithFacets=true'

response = requests.get(url, headers=headers).json()
print(response)
res = response['filters']
    # response.encoding = 'utf-8'
    # soup = BeautifulSoup(response.text, 'lxml')
    # print(soup)
    # #div = soup.find_all('p')
    # #print(div)

#    response = requests.get(url=url, headers=headers).json()
#     if response['next'] == None:
#         break
#     else:
#         res = response['results']
#         #print(res)
#         for r in res:
#
#             #print(r)
#             s = ' '
#             discount = math.ceil(100 - (r['current_prices']['price_promo__min']/r['current_prices']['price_reg__min']*100))
#             #discount = math.ceil(discount)
#             position = str(r['name']+'\n') + str(r['promo']['date_end']) + '\n'+ str(r['current_prices']['price_promo__min']) + ' / ' + str(r['current_prices']['price_reg__min']) + '\n' + str(r['img_link'])
#
#             if discount > 30:
#                 position_add = position + '\nСкидка: ' + str(math.ceil(discount)) + '%\n'
#                 # print(position)
#                 # print('Скидка: ' + str(math.ceil(discount)) + '%\n')
#                 print(position_add)
#                 list = list + position_add + '\n'
#
#
#
# with open('5ka.txt', 'w') as f:
#     f.write(list)





