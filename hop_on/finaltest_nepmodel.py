from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests
import os


html = urlopen('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')
soup = BeautifulSoup(html, 'html.parser')
#images = soup.find_all('img', {'src':re.compile('.jpg')})

for post in soup.find_all('tbody'):
        for post_content in post.find_all("td"):
            print(post_content['a[href]'])
            for pic in post_content.find_all("img"):
                print(pic['src'])