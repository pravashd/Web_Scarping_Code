import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('B2bexpos-directory.csv', 'w'))
f.writerow(['Company Name','Description','Telephone','Links'])
dash = ["https://www.iomchamber.org.im/members/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soups = BeautifulSoup(r.content, 'html.parser')
 companysData1234 = soups.select('div[class="container clearfix"] > nav[class="pagination"] > ul > li > a')
 for companyName in companysData1234:
     links = companyName.get("href")
     rr1 = requests.get(links)	
     soups789 = BeautifulSoup(rr1.content, 'html.parser')
     print(links)
