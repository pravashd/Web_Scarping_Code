import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('Nn-directory.csv', 'w'))
f.writerow(['Links','Title','Telephone','Categories'])

dash = ["https://www.jtdirectory.com/listing/view/471263/a1-aerials-satellite-systems"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="main-info col-sm-4"]')
 for company in companysData:
     for title in company.select('div[class="block-title"] > h3'):
         title = title.text
         print(title)
     for add in company.select('div[class="box-ico btn-marker"]'):
         add = add.text
         print(add)
     
     
