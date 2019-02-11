import lxml
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

def test():
    url = "https://asheville.craigslist.org/search/fua"
    driver = webdriver.Firefox()
    driver.get(url)
    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "lxml")
    for post in soup.find_all('li', "result-row"):
        for post_content in post.find_all("a", "result-image gallery"):
            print(post_content['href'])
            for pic in post_content.find_all("img"):
                print(pic['src'])