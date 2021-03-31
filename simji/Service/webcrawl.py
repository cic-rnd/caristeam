import urllib.request
from bs4 import BeautifulSoup
from Util.Info import *


html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')


result = soup.title.string


print(result)
