import requests
from bs4 import BeautifulSoup as BS
import lxml

url = 'https://finance.ua/'
r = requests.get(url)
soup = BS(r.text, 'lxml')
curs = soup.find_all("span", { "class" : "fua-xrates__value"})

print(curs)
