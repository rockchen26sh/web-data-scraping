#coding = UTF-8
from urllib.request import urlopen
import re
from bs4 import BeautifulSoup

url = "https://www.ebates.cn/"

html = urlopen(url)
bsObj = BeautifulSoup(html)
value = bsObj.get_text()
print(value)
