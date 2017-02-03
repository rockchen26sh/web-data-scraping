from bs4 import BeautifulSoup
from urllib.request import urlopen

html = urlopen("http://javopen.co")
bsObj = BeautifulSoup(html)
test = bsObj.get_text()
print(test)
