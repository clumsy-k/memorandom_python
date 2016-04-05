#! /usr/bin/env python

from urllib2 import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html, "html.parser")

allText = bsObj.findAll(id="title", class="text")
print(allText[0].get_text())
