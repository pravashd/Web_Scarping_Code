import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('m-directory.csv', 'w'))
f.writerow(['links','Title','Address','Telephone/Fax','Aboutus'])

dash = ["https://www.iomchamber.org.im/members/?Page=1&","https://www.iomchamber.org.im/members/?Page=&"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class="members-list"] > div[class="standard-member"]')
 companylinks = soup.select('nav[class="pagination"] ul > li > a')
 for companyinfo in companylinks:
     companylinks = 'https://www.iomchamber.org.im/members/'+companyinfo.get('href')
     companylinkss = requests.get(companylinks)		# r variable has all the HTML code
     companylinksSoup = BeautifulSoup(companylinkss.content, 'html.parser')
 for title in companylinksSoup.select('div[class="member-content"] > h3'):
     title = title.text 
     print(title)         
 for add in companylinksSoup.select('div[class="member-content"] > p'):
     add = add.text 
     print(add)

