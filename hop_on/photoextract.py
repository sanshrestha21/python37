from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', {'src':re.compile('.jpg')})
for image in images: 
    print(image['src']+'\n')
        