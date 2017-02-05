from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen("http://pythonscraping.org/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile = StringIO(data)
csvReader = csv.reader(dataFile)

for row in csvReader:
    print(row)
    print(row)