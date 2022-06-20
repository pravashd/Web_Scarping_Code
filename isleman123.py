import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('AtZ-islecom.csv', 'w'))
f.writerow(['Links','Title','Address','Telephone/Fax','Category'])

dash = ["https://www.isleofman.com/directory/AToZ/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="azselect-home"] > ul > li > a')
 for company in companysData:
     links = 'https://www.isleofman.com/directory/AToZ/'+company.get('href') 
     companylist = requests.get(links)		# r variable has all the HTML code
     companySoup = BeautifulSoup(companylist.content, 'html.parser')
     companylinks = companySoup.select('div[class="azlist"] > ul > li > a')
     for companyinfo in companylinks:
         companylinks = 'https://www.isleofman.com/directory/AToZ/'+companyinfo.get('href')
         companylinkss = requests.get(companylinks)		# r variable has all the HTML code
         companylinksSoup = BeautifulSoup(companylinkss.content, 'html.parser')
         companylinksfile = companylinksSoup.select('div[class="listing-left"] > h3 > a')
     for companyfile in companylinksfile:
          compfile = 'https://www.isleofman.com/directory/AToZ/'+companyfile.get('href') 
          companyfilelist = requests.get(compfile)		# r variable has all the HTML code
          companyfieSoups = BeautifulSoup(companyfilelist.content, 'html.parser')
          for title in companyfieSoups.select('div[class="entry-overview"] > h1'):
              title = title.text.strip()
          for add in companyfieSoups.select('div[class="col-left"] > p[class="listing-add"]'):
              add = add.text.strip()
          for telephone in companyfieSoups.select('ul[class="listing-cont"] > li'):
              telephone = telephone.text.strip() 
          for about in companyfieSoups.select('div[class="more-about-us"] > p'):
              about = about.text.strip()   
          for categories in companyfieSoups.select('div[class="listing-category"] > p'):
              categories = categories.text.strip()
              info = [compfile,title,add,telephone,categories]
              print(info)
              f.writerow(info)


