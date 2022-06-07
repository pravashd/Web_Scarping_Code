import requests
from bs4 import BeautifulSoup
from csv import writer

url = ["https://www.weareguernsey.com/business-directory/?qb=&cat=1000",
      "https://www.weareguernsey.com/business-directory/?qb=&cat=1004","https://www.weareguernsey.com/business-directory/?qb=&cat=1006","https://www.weareguernsey.com/business-directory/?qb=&cat=1011","https://www.weareguernsey.com/business-directory/?qb=&cat=1053","https://www.weareguernsey.com/business-directory/?qb=&cat=1013","https://www.weareguernsey.com/business-directory/?qb=&cat=1015"]

with open('webscraping.csv','w', encoding='utf8', newline='') as f:
     thewriter = writer(f)
     header = ['Company Name', 'Company Website', 'Company Phone Number', 'Company Description']
     thewriter.writerow(header)	

for urls in url:
   r = requests.get(urls)		# r variable has all the HTML code
   soup = BeautifulSoup(r.content, 'html.parser')
   companysData = soup.select('div[class*="fx-sm-3 fx-lg-4 listing"]')
   for company in companysData:
         ul = company.find("span", attrs= {"class":'service'})
         links = "https://www.weareguernsey.com/"+ul.parent.get('href')
         rr = requests.get(links)		# r variable has all the HTML code
         soups = BeautifulSoup(rr.content, 'html.parser')
         companyName = soups.select('div[class="mw-1000"]> h1').text.replace('\n','')  
         companyWebsite = soups.select('h2[class="web"]> a').text.replace('\n','') 
         companyPhone = soups.select('div[class="mw-1000 flex"]').text.replace('\n','') 
         companyDescription = soups.select('div[class="biz-detail-copy"]').text.replace('\n','') 
         info = [companyName, companyWebsite, companyPhone, companyDescription]  
         thewriter.writerow(info)
print(f.closed) 
