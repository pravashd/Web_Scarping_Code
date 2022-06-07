import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('m-directory.csv', 'w'))
f.writerow(['Links','Title','Address','Telephone/Fax'])

dash = ["https://www.directory.im/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azselect-home"] > ul > li > a')
 for company in companysData:
     links = 'https://www.directory.im'+company.get('href') 
     companylist = requests.get(links)		# r variable has all the HTML code
     companySoup = BeautifulSoup(companylist.content, 'html.parser')
     companylinks = companySoup.select('div[class="azlist"] > ul > li > a')
     for companyinfo in companylinks:
      companylinks = 'https://www.directory.im'+companyinfo.get('href')
      companylinkss = requests.get(companylinks)		# r variable has all the HTML code
      companylinksSoup = BeautifulSoup(companylinkss.content, 'html.parser')
      companylinksfile = companylinksSoup.select('div[class="listing-left"] > h3 > a')
      for companyfile in companylinksfile:
         compfile = 'https://www.directory.im'+companyfile.get('href') 
         companyfilelist = requests.get(compfile)		# r variable has all the HTML code
         companyfieSoups = BeautifulSoup(companyfilelist.content, 'html.parser')
         for title in companyfieSoups.select('div[class="listing-left"] > h1'):
            title = title.text
         for add in companyfieSoups.select('div[class="listing-left"] > p[class="listing-add"]'):
             add = add.text 
         for telephone in companyfieSoups.select('ul[class="listing-cont"] > li'):
             telephone = telephone.text  
             info = [compfile,title,add,telephone]
             print(info)
             f.writerow(info)
             break     



     
