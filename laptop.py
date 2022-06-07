import requests
from bs4 import BeautifulSoup

url = ["https://www.weareguernsey.com/business-directory/?qb=&cat=1000",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1004"]
for urls in url:
   r = requests.get(urls)		# r variable has all the HTML code
   soup = BeautifulSoup(r.content, 'html.parser')
   companysData = soup.select('div[class*="fx-sm-3 fx-lg-4 listing"]')
   for company in companysData:
         ul = company.find("span", attrs= {"class":'service'})
         links = "https://www.weareguernsey.com/"+ul.parent.get('href')
         rr = requests.get(links)		# r variable has all the HTML code
         soups = BeautifulSoup(rr.content, 'html.parser')
         for companyName in soups.select('div[class="mw-1000"] > h1'):
            print(companyName.text) 
         for companyWebsite in soups.select('h2[class="web"] > a'):
            print(companyWebsite.text)   
         for companyPhone in soups.select('div[class="mw-1000 flex"]'):
            print(companyPhone.text)  
         for companyDescription in soups.select('div[class="biz-detail-copy"]'):
            print(companyDescription.text)
      
