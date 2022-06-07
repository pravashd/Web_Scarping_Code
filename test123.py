import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('d-csv1.csv', 'w'))
f.writerow(['text','inner text'])

dash = ["http://www.directory.im/atla-accountancy-services-limited_s1795"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="listing-left"] > h1')
 for company in companysData:
     print(company) 

