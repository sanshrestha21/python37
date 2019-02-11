import sys
#from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl
#from PyQt5.QtWebKitWidgets import QWebPage
from PyQt5.QtWebEngineWidgets import QWebEngineView as QWebView,QWebEnginePage as QWebPage
from lxml import html

#Take this class for granted.Just use result of rendering.
class Render(QWebPage):
  def __init__(self, url):
    self.app = QApplication(sys.argv)
    QWebPage.__init__(self)
    self.loadFinished.connect(self._loadFinished)
    self.mainFrame().load(QUrl(url))
    self.app.exec_()

  def _loadFinished(self, result):
    self.frame = self.mainFrame()
    self.app.quit()

url = 'http://pycoders.com/archive/'
r = Render(url) 
result = r.frame.toHtml()
htmltree = html.fromstring(result)
archive_links = htmltree.xpath('//div[2]/div[2]/div/div[@class="campaign"]/a/@href')
print(archive_links)