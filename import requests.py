import requests
from bs4 import BeautifulSoup
from csv import writer

url = ["https://www.directory.im/",
      "http://www.directory.im/cat_accountants/nc33862"]

with open('web-1-scraping.csv','w', encoding='utf8', newline='') as f:
     thewriter = writer(f)
     header = ['Company Name', 'Company Website']
     thewriter.writerow(header)	
     
for urls in url:
   r = requests.get(urls)		# r variable has all the HTML code
   soup = BeautifulSoup(r.content, 'html.parser')
   companysData = soup.select('div[class*="azselect-home"]')
   for company in companysData:
         ul = company.find("span", attrs= {"class":'featured-bus-panel'})
         links = "https://www.directory.im/"+ul.parent.get('href')
         
