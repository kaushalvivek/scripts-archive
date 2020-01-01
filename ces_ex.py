import requests
import csv
from bs4 import BeautifulSoup
import re

data = []
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

url = "/Users/vivekkaushal/Desktop/index.htm"
try:
  # r = requests.get(url, headers=headers, timeout=5)
  page = open(url)
except:
  print('Could not reach website')
  quit()

data =[]

soup = BeautifulSoup(page, 'html.parser')
# articles = soup.find("article", {"id": "speaker-listing"})
company = soup.find_all("div",{"class": "exhibitorRow listingCard p-2 bd-highlight"})
for i in company:
  name = i.find('a').contents[0]
  link = i.find('a')['href']
  footer = i.find('footer')
  booth = footer.find('a').contents[0]
  data_dict = {
    'name':name,
    'link':link,
    'booth':booth
  }
  data.append(data_dict)


keys = data[0].keys()
with open('data.csv', 'w+') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(data)

print("CSV Written")