from urllib.request import urlopen
import re
import random
from bs4 import BeautifulSoup
import requests
import time
import pymysql

conn = pymysql.connect(host="127.0.0.1",user='root',passwd='28488747',db = 'scraping',use_unicode='True',charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

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
    try:
        req = session.get(url,headers=header)
        bsObj_info = BeautifulSoup(req.text)
        content = bsObj_info.find("div",{"class":"post-content img-max-size"}).get_text()
        category = bsObj_info.find("ul",{"class":"info"}).findAll("li")[2].find("span").get_text()
        brand = bsObj_info.find("ul",{"class":"info"}).findAll("li")[4].get_text()
        mall = bsObj_info.find("ul",{"class":"info"}).findAll("li")[5].get_text()
        brand = brand.replace("品牌 ","")
        mall = mall.replace("商城 ","")
        total = {"brand":brand,"content":content,"mall":mall,"category":category}
        print(category)
        return total
    except AttributeError:
        print(bsObj_info)
        return {"brand":'-',"content":'-',"mall":'-',"category":'-'}

def insert_data(brand,title,price,content,mall,category):
    cur.execute("INSERT INTO mgpyh (Brand,Title,Price,Content,Mall,Category) VALUE (%s,%s,%s,%s,%s,%s)",
                    (brand, title, price, content, mall,category))
    conn.commit()



while True :
    n = 0
    for i in range(1,2):

        url = "https://www.mgpyh.com/post/?page=" + str(i)
        items = get_items(url)
        for item in items:
            if n > 2:
                break
            href = item.find("a",{"class":"readmore"})["href"]
            title = item.find("a").get_text()
            try:
                price = item.find("em").get_text()
            except AttributeError:
                price = 0
            print(title)
            #time.sleep(5)
            item_info = get_item_info("https://www.mgpyh.com" + href)
            brand = item_info["brand"]
            content = item_info["content"]
            mall = item_info["mall"]
            category = item_info["category"]
            cur.execute("SELECT * from mgpyh WHERE Title = %s",(title))
            if cur.rowcount == 0 :
                insert_data(brand, title, price, content, mall,category)
            else:
                n += 1

            time.sleep(3)
            print(i)
            print (n)
    time.sleep(random(600,900))

cur.close()
conn.close()


