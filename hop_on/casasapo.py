from bs4 import BeautifulSoup
from requests import get
import pandas as pd
import itertools 
import urllib.request
import datetime 

headers = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.96 Safari/537.36'})

sapo = 'https://casa.sapo.pt/Venda/Apartamentos/?sa=11&lp=10000&or=10'
response = get(sapo, headers=headers)
#print(response.text[:1000])
##find tag
html_soup = BeautifulSoup(response.text, 'html.parser')

# house_containers = html_soup.find_all('div', class_='searchPropertyPrice')
# ##find contain text on that tag
# first = house_containers[0]
# first.find_all('span')
# print(first)
# print("############")
# ##strip to more readable format
# var_1 = first.find_all('span')[0].text
# print(var_1)
# print("###########")
# ##replace umwanted tex and symbols
# var_1 = var_1.replace('\xa0', '')
# print(var_1)
# ####usinf itertool to retrieve the digit value only
# ###Price of Aparment is obtained
# var_1 = int(''.join(itertools.takewhile(str.isdigit, var_1)))
# print(var_1)#, type(var_1))

###Location
#second = location_containers[0]
# location_containers = html_soup.find_all('p', class_='searchPropertyLocation')[3].text

# #second = location_containers[0]
# #second.find_all('font')
# # #location = first.find_all('p',class_='searchPropertyLocation')
# #var_2 = second.find_all('font').text
# #print(var_2)
# #second = location_containers[7:location_containers.find(',')]
# print(location_containers)
####size in m2
# size = html_soup.find_all('div',class_='searchPropertyInfo')
# s_size = size[0]
# #var_2 = s_size.find_all('p')
# var_2 = s_size.find_all('p')[3].text
# var_2 = int(''.join(itertools.takewhile(str.isdigit, var_2)))
# print(var_2, type(var_2))

####print first 10 searchpropertyinfo values
#print(var_2[:10])
####img
image_contain = html_soup.find_all('div',class_='searchResultProperty')
first = image_contain[0]
first.find_all('div',class_='photoContainer')
print(first[:10])
# print(image_contain[:10])
# first = image_contain[0]
# first.find_all('img')
# print(first)
# house_containers = html_soup.find_all('div', class_='searchPropertyPrice')
# ##find contain text on that tag
# first = house_containers[0]
# first.find_all('span')
# print(first)

