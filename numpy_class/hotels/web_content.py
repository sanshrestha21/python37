import urllib2
import html2text
url='https://www.oyorooms.com/search?location=Pokhara%2C%20Gandaki%2C%20Nepal&city=Pokhara&searchType=city&checkin=22%2F03%2F2019&checkout=23%2F03%2F2019&roomConfig%5B%5D=1&country=nepal&guests=1&rooms=1&filters%5Bcity_id%5D=549'
page = urllib2.urlopen(url)
html_content = page.read()
rendered_content = html2text.html2text(html_content)
file = open('web_page.txt', 'w')
file.write(rendered_content)
file.close()