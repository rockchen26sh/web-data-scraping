from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import random
import datetime

pages = set()
random.seed(datetime.datetime.now())

#获取网站内链的列表
def getInternalLinks(bsobj,includeUrl):
    includeUrl = urlparse(includeUrl).scheme+"://" + urlparse(includeUrl).netloc
    internalLinks = []
    #找出以/开头的链接
    for link in bsobj.findAll("a",href = re.compile("^(/|.*" + includeUrl + ")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith("/")):
                    internalLinks.append(includeUrl+link.attrs['href'])
                else:
                    internalLinks.append(link.attrs['href'])
    return internalLinks

#获取网站所有外链列表
def getExternalLinks(bsobj,excludeUrl):
    externalLinks = []
    for link in bsobj.findAll("a",href = re.compile("^(http|www)((?!"+excludeUrl + ").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in excludeUrl:
                externalLinks.append(link.attrs['href'])
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://","").split("/")
    return addressParts

def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsobj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsobj,urlparse(startingPage).netloc)
    if len(externalLinks) == 0:
        print("No external links, looking around the site for one")
        domain = urlparse(startingPage).scheme + "://" +rulparse(startingPage).netloc
        internalLinks = getInternalLinks(bsobj,domain)
        return getRandomExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0,len(externalLinks)-1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is : " + externalLink)
    followExternalOnly(externalLink)


from pandas import Series
allExtLinks = []
allIntLinks = []
def getAllExternalLinks(siteUrl):
    html = urlopen(siteUrl)
    bsObj = BeautifulSoup(html)
    internalLinks = getInternalLinks(bsObj,splitAddress(siteUrl)[0])
    externalLinks = getExternalLinks(bsObj,splitAddress(siteUrl)[0])
    for link in externalLinks:
        if link not in allExtLinks:
            allExtLinks.append(link)
            print(link)
    for link in internalLinks:
        if link not in allIntLinks:
            allIntLinks.append(link)
            print(link)

getAllExternalLinks("http://oreilly.com")

print(allExtLinks,'---','\n',allIntLinks)
