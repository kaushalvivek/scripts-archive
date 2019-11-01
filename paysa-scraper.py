import requests
import os
from bs4 import BeautifulSoup

temp = open('test.html', 'w+')
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}

query = ['google.'
,'apple'
,'facebook'
,'microsoft'
,'amazon'
,'paypal'
,'adobe'
,'intel'
,'oracle'
,'samsung'
,'yahoo'
,'ibm'
,'nintendo'
,'blackberry'
,'twitter'
,'cisco'
,'electronic-arts'
,'nvidia'
,'dell-technologies'
,'htc'
,'airbnb'
,'uber'
,'netfilx'
,'palantir'
,'wework'
,'spacex'
,'dropbox'
,'snapchat'
,'xiaomi'
,'pinterest'
,'flipkart'
,'paytm'
,'snapdeal'
,'swiggy'
,'ola'
,'bigbasket'
,'hike-messenger'
,'oyorooms'
,'zomato'
,'quikr'
,'infosys'
,'wipro'
,'tcs'
,'congnizant'
,'tech-mahindra'
,'hcl-technologies'
,'l&t-infotect'
,'capgemini'
,'accenture'
,'honeywell'
,'visa'
,'dbs'
,'morgan-stanley'
,'tower-research'
,'ubs'
,'mckinsey-and-company'
,'bain-and-company'
,'d。-e。-shaw-research'
,'goldman-sachs'
,'ernst-&-young']
for i in range (0, len(query)) :
    url = "https://www.paysa.com/salaries/"+query[i]+"--software-engineer"
    r = requests.get(url, headers=headers, timeout=5)
    soup = BeautifulSoup(r.text, 'html.parser')
    temp.write(str(soup))
    base = soup.find('meta', { "name" : "description" }) 
    temp.close()
    pointer = str(base['content']).find('$')
    print(str(base['content'])[pointer:pointer+4].strip())