import urllib.request as request
import requests
import os
from bs4 import BeautifulSoup
import re

url = requests.get('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')
soup = BeautifulSoup(url.content, 'lxml')
#print(soup)
img_url = [i['href'] for i in soup.select('a[href]')]
print(img_url)
# anna_img_url = [i for i in img_url if re.search('ekta', str(i))]
# #print(anna_img_url)
# if not os.path.exists('ekta'):
#     os.makedirs('ekta')

# for i in anna_img_url:
#     with open('ekta/' + os.path.split(i)[1], 'wb') as f:
#         print(i)
#         f.write(requests.get(i).content)