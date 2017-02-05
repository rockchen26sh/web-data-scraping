from urllib.request import urlopen
import re
import random
from bs4 import BeautifulSoup
import requests

session = requests.Session()
header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
          "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
          "Accept-Encoding":"gzip,deflate,sdch",
          "Accept-Kabgyage":"zh-CN,zh;q=007,ja;q=0.6"}

def get_items(url):
    req = session.get(url, headers=header)
    bsObj = BeautifulSoup(req.text)
    items = bsObj.findAll("div",{"class":"content-item clearfix"})
    return items

def get_item_info(url):
    req = session.get(url,headers=header)
    bsObj_info = BeautifulSoup(req.text)
    content = bsObj_info.findAll("div",{"class":"post-content img-max-size"})[0].get_text()
    brand = bsObj_info.find("ul",{"class":"info"}).findAll("li")[4].get_text()
    brand = brand.replace("品牌 ","")
    total = {"brand":brand,"content":content}
    return total


url = "https://www.mgpyh.com/post/?page=1"
items = get_items(url)

for item in items:
    href = item.find("a",{"class":"readmore"})["href"]
    title = item.find("a").get_text()
    title1 = title.split("￥")[0]
    price = title.split("￥")[1]
    item_info = get_item_info("https://www.mgpyh.com" + href)
    brand = item_info["brand"]
    content = item_info["content"]
    print(title1,"|",price,"|",brand,"|",content,"|")


