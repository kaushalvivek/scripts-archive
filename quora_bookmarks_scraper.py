import os
from bs4 import BeautifulSoup

file = open('output.txt','w+')
r = open('./bookmarked_answers','r')
soup = BeautifulSoup(r, 'html.parser')
all_a = soup.find_all('a')
print(all_a)
for i in range (0,len(all_a)):
    if all_a[i].get('class') != None:
        if 'question_link' in all_a[i].get('class'):
            file.write(str(all_a[i]))