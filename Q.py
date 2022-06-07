import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('G-telephone.csv', 'w'))
f.writerow(['Telephone','Mobile'])

dash = ["https://www.isleofman.com/directory/AToZ/G"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azlist"] > ul > li > a')
 for company in companysData:
     links = 'https://www.isleofman.com/directory/AToZ/G'+company.get('href') 
     rr1 = requests.get(links)		# r variable has all the HTML code
     soups = BeautifulSoup(rr1.content, 'html.parser')
     companysData123 = soups.select('div[class="listing-left"] > h3 > a')
     for company12345 in companysData123:
        links456 = 'https://www.isleofman.com/directory/AToZ/G'+company12345.get('href') 
        rr123 = requests.get(links456)
        soups789 = BeautifulSoup(rr123.content, 'html.parser')	
        telephone = soups789.select('ul[class="listing-cont"] > li')
        telephone = telephone[-1].text 
        mobile = soups789.select('ul[class="listing-cont"] > li')
        mobile = mobile[0].text 
        info = [telephone,mobile]
        print(info)
        f.writerow(info)


