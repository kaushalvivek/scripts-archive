import os,requests
from bs4 import BeautifulSoup

agefile = open("age.txt","w+") 
query = ['Alphabet+Inc.'
,'Apple+Inc.'
,'Facebook+Inc.'
,'Microsoft'
,'Amazon'
,'PayPal'
,'Adobe'
,'Intel'
,'Oracle'
,'Samsung'
,'Yahoo'
,'IBM'
,'Nintendo'
,'Blackberry'
,'Twitter'
,'Cisco'
,'Electronic+Arts'
,'Nvidia'
,'Dell+Technologies'
,'HTC'
,'AirBnB'
,'Uber'
,'Netflix'
,'Palantir'
,'WeWork'
,'SpaceX'
,'Dropbox'
,'Snap+Inc.'
,'Xiaomi'
,'Pinterest'
,'Flipkart'
,'PayTM'
,'Snapdeal'
,'Swiggy'
,'Ola'
,'Bigbasket'
,'Hike+Messenger'
,'OYORooms'
,'Zomato'
,'Quikr'
,'Infosys'
,'Wipro'
,'TCS'
,'Congnizant'
,'Tech+Mahindra'
,'HCL+Technologies'
,'L&T+Infotech'
,'Capgemini'
,'Accenture '
,'Honeywell'
,'VISA'
,'DBS'
,'Morgan+Stanley'
,'Tower+Research'
,'UBS'
,'McKinsey+and+Company'
,'Bain+and+Company'
,'DE+Shaw+&+Co'
,'Goldman+Sachs'
,'Ernst+&+Young+LLP']

# What to do:
# For each query -
#     Search google with 'Wiki' as pre
#     click on first link
#     on that page that opens search for founded cell
#     store now().year - that date
#     that date is the age
#     Store in some external file serially

for k in range (0,60):
    r = requests.get("https://www.google.co.in/search?q=wiki+"+query[k])
    soup = BeautifulSoup(r.text, 'html.parser')
    tag = soup.h3
    linktag = tag.a
    r2 = requests.get("http://google.co.in/"+linktag.attrs['href'])
    wiki = BeautifulSoup(r2.text,'html.parser')
    ptag = wiki.table
    if (ptag == None):
        continue
    alltr = ptag.find_all('tr')
    count = len(alltr)

    for i in range (0,count):
        if alltr[i].th != None:
            if alltr[i].th.get_text()=='Founded':
                agefile.write(str(query[k])+' : '+str(alltr[i].td.get_text()+'\n'))
                print (str(query[k])+' : '+str(alltr[i].td.get_text()))

agefile.close()
# os.system("open -a 'Google Chrome' https://www.google.co.in/search?q=wiki+"+query[0])
