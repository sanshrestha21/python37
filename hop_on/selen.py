# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
 
# options = webdriver.ChromeOptions()
# options.add_argument('--ignore-certificate-errors')
# #options.add_argument("--test-type")
# chrome_options = Options()
# chrome_options.add_argument("--disable-extensions")
# #options.binary_location = "/usr/bin/chromium"
# driver = webdriver.Chrome(chrome_options=options)

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
driver = webdriver.Chrome(chrome_options=chrome_options)
 
driver.get('http://www.cybersansar.com/thumbnail_view.php?gal_id=2278')
 
images = driver.find_elements_by_tag_name('img')
for image in images:
    print(image.get_attribute('src'))
 
driver.close()