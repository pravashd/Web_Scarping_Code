import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('A-a2z-isleofman_com.csv', 'w'))
f.writerow(['Links','Title','Address','Telephone','Category'])

dash = ["https://www.isleofman.com/directory/AToZ/A"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azlist"] > ul > li > a')
 for company in companysData:
     links = 'https://www.isleofman.com/directory/AToZ/B'+company.get('href') 
     rr1 = requests.get(links)		# r variable has all the HTML code
     soups = BeautifulSoup(rr1.content, 'html.parser')
     companysData123 = soups.select('div[class="listing-left"] > h3 > a')
     for company12345 in companysData123:
        links456 = 'https://www.isleofman.com/directory/AToZ/B'+company12345.get('href') 
        rr123 = requests.get(links456)
        soups789 = BeautifulSoup(rr123.content, 'html.parser')	
        for title in soups789.select('div[class="entry-overview"] > h1'):
            title = title.text.strip()
        adds= ''
        for add in soups789.select('div[class="col-left"] > p[class="listing-add"]'):
            if(add.text != ''):
               adds = add.text.strip()
        for telephone in soups789.select('ul[class="listing-cont"] > li > strong'):
            telephone = telephone.text.strip()
        for categories in soups789.select('div[class="listing-category"] > p > a'):
            categories = categories.text.strip()
            info = [links456,title,adds,telephone,categories]
            print(info)
            f.writerow(info)
