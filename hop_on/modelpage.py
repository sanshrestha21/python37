from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()
# it takes forever to load the page, therefore we are setting a threshold
driver.set_page_load_timeout(5)

try:
    driver.get("http://www.cybersansar.com/thumbnail_view.php?gal_id=2278")
except TimeoutException:
    # never ignore exceptions silently in real world code
    pass

soup2 = BeautifulSoup(driver.page_source, 'html.parser')
divImage = soup2.find('div', {"td": "photolink"})

# close the browser 
driver.close()

for img in divImage.findAll('img'):
    print (img.get('src'))