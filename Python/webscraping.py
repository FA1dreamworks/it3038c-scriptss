from bs4 import BeautifulSoup
import requests, re

r = requests.get('https://analytics.usa.gov').content
soup= BeautifulSoup(r, 'html.parser')
print(type(soup))
for link in soup.find_all('a'): print(link.get('href'))