import requests
import csv
from bs4 import BeautifulSoup
import re

data = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = "/Users/vivekkaushal/Downloads/file.htm"
try:
  # r = requests.get(url, headers=headers, timeout=5)
  page = open(url)
except:
  print('Could not reach website')
  quit()

soup = BeautifulSoup(page, 'html.parser')
articles = soup.find("article", {"id": "speaker-listing"})
aside = articles.find_all("aside")
for i in aside:
  link = i.find('a')['href']
  name = i.find('h3').text
  details = i.find_all('h4')
  points = {
    "link": "https://ces.tech"+str(link),
    "name":name,
    "company":details[1].text,
    "position":details[0].text
  }
  data.append(points)

keys = data[0].keys()
with open('data.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)

print("CSV Written")