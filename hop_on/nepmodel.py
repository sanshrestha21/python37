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


#for image in images: 

for image in images:
    #print(image['src']+'\n')
    model_image = [image['src']]
    #model_image=model_image.append(model_image)
    #print(model_image)
    ekta_img_url = [i for i in model_image if re.search('ekta', str(i))]
    #print(ekta_img_url)
#print("#############")
    for data in ekta_img_url:
        imgurl="http://cybersansar.com/"+data+""
        imgurl=imgurl.replace("/thumb","")
        #print(imgurl)


        tokens=imgurl.split("/")
        file_name=tokens[len(tokens)-1]
        file=open(file_name,"w+")
        file.close()
# if not os.path.exists('Ekta'):
#     os.makedirs('Ekta')

# for i in data:
#     with open('Ekta/' + os.path.split(i)[1], 'wb') as f:
#         print(i)
#         f.write(requests.get(i).content)

    #i=[]
#print("############")

# for i in model_image:
#     #i=[re.search('ekta', model_image,"wb")]
#     i = [re.search(r'\bekta_kunwar\w+', i)]
# #     #i.append
#     print(i)
#print(['Ekta_img_url'] +'\n')

#bs = BeautifulSoup(html, 'html.parser')
#images = bs.find_all('img', {'src':re.compile('.jpg')})
# for image in images: 
#     print(image['src']+'\n')

# if not os.path.exists('Ekta'):
#     os.makedirs('Ekta')

# for i in Ekta_img_url:
#     with open('Ekta/' + os.path.split(i)[1], 'wb') as f:
#         print(i)
#         f.write(requests.get(i).content)