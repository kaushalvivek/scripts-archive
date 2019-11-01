import requests
import os
from bs4 import BeautifulSoup

r = requests.get("https://www.iiit.ac.in/people/faculty/")
soup = BeautifulSoup(r.text, 'html.parser')
all_h3 = soup.find_all('h3')
all_href=[]
for i in range (0, len(all_h3)):
    all_href.append ("https://iiit.ac.in"+all_h3[i].a['href'])
print (all_href)