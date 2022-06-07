import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('z-artist-names.csv', 'w'))
f.writerow(['links','Company Name', 'Website', 'Phone Number', 'Description'])

dash = ["https://www.weareguernsey.com/business-directory/?qb=&cat=1000",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1004",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1006",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1011",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1053",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1013",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1024",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1026",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1033",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1035",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1037",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1038",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1040",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1051",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1052",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1006&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1053&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1013",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=3",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=4",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=5",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1053&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=3",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=4",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1015&page=5",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1026&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1035&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1040&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044&page=2",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044&page=3",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044&page=4",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044&page=5",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1044&page=6"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class*="fx-sm-3 fx-lg-4 listing"]')
 for company in companysData:
      ul = company.find("span", attrs= {"class":'service'})
      links = "https://www.weareguernsey.com"+ul.parent.get('href')
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
      print(info)
      f.writerow(info)