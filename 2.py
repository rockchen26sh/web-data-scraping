# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsobj = BeautifulSoup(html)

#抽取只包含span class = green 标签里的文字
nameList = bsobj.findAll("span",{'class':'green'})
for name in nameList:
    print(name.get_text())

#查找“the prince”内容的标签数量
nameList = bsobj.findAll(text = "the prince")
print(len(nameList))

#选择制定属性的标签
allText = bsobj.findAll(id = "text")
print(allText[0].get_text())

