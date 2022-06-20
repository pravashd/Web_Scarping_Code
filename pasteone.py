import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['links','Company Name', 'Website', 'Phone Number', 'Description'])

dash = ["https://www.weareguernsey.com/business-directory/?qb=&cat=1000",
"https://www.weareguernsey.com/business-directory/?qb=&cat=1006"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class*="fx-sm-3 fx-lg-4 listing"]')
 for company in companysData:
      ul = company.find("span", attrs= {"class":'service'})
      links = "https://www.weareguernsey.com/"+ul.parent.get('href')
      rr = requests.get(links)		# r variable has all the HTML code
      soups = BeautifulSoup(rr.content, 'html.parser')
      for companyName in soups.select('div[class="mw-1000"] > h1'):
          companyNames = companyName.text 
      for companyWebsite in soups.select('h2[class="web"] > a'):
          companyWebsites = companyWebsite.text   
      for companyPhone in soups.select('div[class="mw-1000 flex"]'):
          companyPhones = companyPhone.text  
      for companyDescription in soups.select('div[class="col-xs-12"] > div[class="mw-1000"] > div[class="biz-detail-copy"]'):
          companyDescriptions = companyDescription.text
          break
      info = [links,companyNames, companyWebsites, companyPhones,companyDescriptions]
      f.writerow(info)

dash = ["https://www.directory.im/","http://www.directory.im/atla-accountancy-services-limited_s1795"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="content"]')
 companysDatass = soup.select('div[class="azselect-home"] > ul > li > a')
 for links in companysDatass:
      links = 'https://www.directory.im'+links.get('href')
for title in soup.select('div[class="listing-left"] > h1'):
    title = title.text
for address in soup.select('div[class="listing-left"] > p'):
    address = address.text
for phone in soup.select('div[class="listing-left"] > ul > li'):
    phone = phone.text.replace('\n','')
for point in soup.select('ul[class="feature-list"] > li'):
    point = point.text
for description in soup.select('div[class="more-about-us"]> p'):
    description = description.text
for description123 in soup.select('div[class="more-contact-item"]> p'):
    description123 = description123.text
info = [links,title, address, phone,description,description123]
print(info)
f.writerow(info)
