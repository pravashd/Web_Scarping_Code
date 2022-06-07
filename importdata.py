import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('d-csv1.csv', 'w'))
f.writerow(['text','inner text'])

dash = ["https://www.directory.im/","http://www.directory.im/atla-accountancy-services-limited_s1795"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="content"]')
 companysDatass = soup.select('div[class="azselect-home"] > ul > li > a')
for company in companysDatass:
     print('https://www.directory.im'+company.get('href') ) 
for companyDD in soup.select('div[class="listing-left"] > h1'):
    companyDD = companyDD
    print(companyDD.get_text())
for companyDDD in soup.select('div[class="listing-left"] > p'):
    companyDDD = companyDDD.text
    print(companyDDD)
for companyDDDD in soup.select('div[class="listing-left"] > ul > li'):
    companyDDDD = companyDDDD
    print(companyDDDD.get_text())
for companyDDDDD in soup.select('ul[class="feature-list"] > li'):
    companyDDDD = companyDDDDD
    print(companyDDDDD.get_text())
for companyDDDDDD in soup.select('div[class="listing-right"]> ul > li'):
    companyDDDD = companyDDDDDD
    print(companyDDDDDD.get_text())
for description in soup.select('div[class="more-about-us"]> h3'):
    description = description
    print(description.get_text())
for description in soup.select('div[class="more-about-us"]> p'):
    description = description
    print(description.get_text())
for description123 in soup.select('div[class="more-contact-item"]> p'):
    description123 = description123
    print(description123.get_text())



