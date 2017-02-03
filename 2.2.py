# coding = utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsobj = BeautifulSoup(html)

for child in bsobj.find("table",{"id":"giftList"}).children:
    print(child)
#选择tr标签的下一个tr标签
for sibling in bsobj.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
#选择src标签，选择src的父标签td，选择td的上一个td标签，获取text
print(bsobj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

#正则表达式
import re

images = bsobj.findAll("img",{"src":re.compile("\.\.\/img/\gifts/\img.*\.jpg")})
for image in images:
    print(image)

