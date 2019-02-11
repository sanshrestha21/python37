import requests
import os
import re
import urllib.request as request
from bs4 import BeautifulSoup

url=requests.get('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')
soup=BeautifulSoup(url.content,'lxml')
pic=soup.find('td',class_='photolink')
pic_numb=pic.find_all('a')
print(pic_numb)

# first=pic[5]
# first.find_all('a')
# print(first)

# img_url=[i['href'] for i in pic.select('a[href]')]
# # print(img_url)
# model_img_url=[i for i in img_url if re.search('ekta_kunwar', str())]
# print(model_img_url)
# if not os.path.exists('ekta_kunwar'):
#     os.makedirs('ekta_kunwar')

# for i in model_img_url:
#     with open('ekta_kunwar/' +os.path.split(i)[1], 'wb') as f:
#         print(i)
#         f.write(requests.get(i).content)

