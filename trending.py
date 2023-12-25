import webbrowser
import time
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


news_url="https://news.google.com/rss"

root=urlopen(news_url)
xml_page=root.read()
soup_page=soup(xml_page,"xml")


soup_page=soup(xml_page,"xml")

news_list=soup_page.findAll("item")

for news in news_list:
    print(news.title.text)

    webbrowser.open(news.title.text, new=len(news_list))
    time.sleep(10)
