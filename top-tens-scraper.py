import os
import requests
from bs4 import BeautifulSoup

print ("Enter name of Artist:")
artist = input()
print ("Enter number of songs you want:")
count = input()
r1 = requests.get("https://www.google.co.in/search?q="+artist+"+thetoptens.com")
soup = BeautifulSoup(r1.text, 'html.parser')
tag = soup.h3
if 'TheTopTens®' in tag.text:
    linktag = tag.a
    r = requests.get("http://google.co.in/"+linktag.attrs['href'])
    soup = BeautifulSoup(r.text, 'html.parser')
    divall = soup.findAll("div", {'class':'i'})
    songs = []
    print("\nFollowing are the results for your request.")
    print("If  an exact list of songs is not found, I try to come up with something close to it.\n")
    for i in range (0, len(divall)) :
        songs.append(divall[i].b.text)

    for i in range (0, min(len(divall),int(count))) :
        print (songs[i])

else:
    print ("Sorry, no associated lists were found for your requests.")
