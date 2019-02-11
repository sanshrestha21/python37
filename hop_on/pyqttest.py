import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
from lxml import html

#Take this class for granted.Just use result of rendering.
# class Render(QWebPage):  
#   def __init__(self, url):  
#     self.app = QApplication(sys.argv)  
#     QWebPage.__init__(self)  
#     self.loadFinished.connect(self._loadFinished)  
#     self.mainFrame().load(QUrl(url))  
#     self.app.exec_()  
  
#   def _loadFinished(self, result):  
#     self.frame = self.mainFrame()  
#     self.app.quit()  
class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = ''
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

def main():
    page = 'http://pycoders.com/issues'
    soup = bs.BeautifulSoup(page, 'html.parser')
    js_test=soup.find('a', class_='my-1 font-weight-normal')
    print(js_test)

print(main)
#if__name__=='__main__': main()

#print(url)
#r = Render(url)  
# result =url.Page.toHtml()
# #This step is important.Converting QString to Ascii for lxml to process
# archive_links = html.fromstring(str(result.toAscii()))
# print(archive_links)