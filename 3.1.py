from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

#随机访问wiki
random.seed(datetime.datetime.now())

#获取herf函数
def getLinks(articleUrl):
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    bsobj = BeautifulSoup(html)
    return bsobj.find("div",{"id":"bodyContent"}).findAll("a",
                        href = re.compile('^(/wiki/)((?!:).)*$'))
#初始链接
links = getLinks("/wiki/Kevin_Bacon")

#递归getlink不断输出随机链接并访问该链接
while len(links)>0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLinks(newArticle)




