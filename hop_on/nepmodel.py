from urllib.request import urlopen
import urllib.request 
from bs4 import BeautifulSoup
import re
import requests
import os


html = urlopen('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')

#content=str(html.read())
bs = BeautifulSoup(html, 'html.parser')

images = bs.find_all('img', {'src':re.compile('.jpg')})

for image in images:
  
    model_image = [image['src']]
    
    #print(model_image)
    ekta_img_url = [i for i in model_image if re.search('ekta', str(i))]
    #print(ekta_img_url)

    for data in ekta_img_url:
        imgurl="http://cybersansar.com/"+data+""
        imgurl=imgurl.replace("/thumb","")
       
        if not os.path.exists('Ekta'):
            os.makedirs('Ekta')
           
        image_test=requests.get(imgurl,stream=True)
        tokens=imgurl.split('/')

        with open('Ekta/' + tokens[len(tokens)-1], 'wb') as f:
            f.write(image_test.content)