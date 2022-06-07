import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('accountant.csv', 'w'))
f.writerow(['links','Title','Address', 'Phone Number','Description','Description123'])

dash = ["https://www.directory.im/","http://www.directory.im/atla-accountancy-services-limited_s1795"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="content"]')
 companysDatass = soup.select('div[class="azselect-home"] > ul > li > a')
 for links in companysDatass:
        llinks = links.get('href')
        rr = requests.get(llinks)		# r variable has all the HTML code
        soups = BeautifulSoup(rr.content, 'html.parser')
        for title in soups.select('div[class="listing-left"] > h1'):
            title = title.text
        for address in soups.select('div[class="listing-left"] > p'):
            address = address.text
        for phone in soups.select('div[class="listing-left"] > ul > li'):
            phone = phone.text
        for point in soups.select('ul[class="feature-list"] > li'):
            point = point.text
        for description in soups.select('div[class="more-about-us"]> p'):
            description = description.text
        for description123 in soups.select('div[class="more-contact-item"]> p'):
            description123 = description123.text
        info = [links,title, address, phone,description,description123]
        print(info)
        f.writerow(info)
