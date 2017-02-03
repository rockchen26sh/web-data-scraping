# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

pages = set()
def getLinks(pageUrl):
    global pages
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsobj = BeautifulSoup(html)
    try:
        print(bsobj.h1.get_text())
        print(bsobj.find(id='mw-content-text').findAll('p')[0])
        print(bsobj.find(id='ca-edit').find("span").find('a').attrs['href'])
    except AttributeError:
        print('页面缺少一些属性！')

    for link in bsobj.findAll('a',href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                newPage = link.attrs['href']
                print("--------\n" + newPage)
                pages.add(newPage)
                getLinks(newPage)

getLinks("")