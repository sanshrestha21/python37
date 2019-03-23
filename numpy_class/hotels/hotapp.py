import requests
from bs4 import BeautifulSoup

url="https://www.oyorooms.com/search?location=Pokhara%2C%20Gandaki%2C%20Nepal&city=Pokhara&searchType=city&checkin=22%2F03%2F2019&checkout=23%2F03%2F2019&roomConfig%5B%5D=1&country=nepal&guests=1&rooms=1&filters%5Bcity_id%5D=549"

def fetch(url):
    resp=requests.get(url)
    return resp.text

soup=BeautifulSoup(fetch(url),"html.parser")
print (soup)