import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('dir-csv1.csv', 'w'))
f.writerow(['links'])

dash = ["https://www.directory.im/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class*="fx-sm-3 fx-lg-4 listing"]')
 for company in companysData:
      ul = company.find("span", attrs= {"class":'contentvwide'})
      links = "https://www.directory.im"+ul.parent.get('href')
      rr = requests.get(links)		# r variable has all the HTML code
      soups = BeautifulSoup(rr.content, 'html.parser')
      for companyName in soups.select('div[class="featured-bus-content"] > h1'):
          companyNames = companyName.text 
      for companyWebsite in soups.select('h2[id="home-mpu"] > a'):
          companyWebsites = companyWebsite.text   
      for companyPhone in soups.select('div[id="azselect-home"]'):
          companyPhones = companyPhone.text  
      for companyDescription in soups.select('div[id="footer-manx"] > div[class="mw-1000"] > div[class="biz-detail-copy"]'):
          companyDescriptions = companyDescription.text
          break
      info = [links,companyNames, companyWebsites, companyPhones,companyDescriptions]
      print(info)
      f.writerow(info)

