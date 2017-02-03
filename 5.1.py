from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup
import os

downloadDirectory = "downloaded"
baseUrl = "http://www.pythonscraping.com"

def getAbsoluteUrl(baseUrl,source):
    if source.startswith("http://www."):
        url = "http://"+source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = "http://" + source[4:]
    else:
        url = baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path = absoluteUrl.replace("www.","")
    path = path.replace(baseUrl,"")
    print(path)
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html)
downloadList = bsObj.findAll(src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl,download["src"])
    if fileUrl is not None:
        print(fileUrl)
        urlretrieve(fileUrl,getDownloadPath(baseUrl,fileUrl,downloadDirectory))
