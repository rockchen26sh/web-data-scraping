from urllib.request import urlopen
from bs4 import BeautifulSoup
def get_Title(url):
    try:
        html=urlopen(url)
    except (HTTPError,URLError) as e:
        return None
    try:
        bsobj = BeautifulSoup(html.read())
        title = bsobj.body.h1
    except AttributeError as e:
        return None
    return title

title = get_Title("http://www.pythonscraping.com/pages/page1.html")

if title = None:
    print("Title could not be found")
else:
    print(title)