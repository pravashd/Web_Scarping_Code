from click import echo
import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('iom_page1234.csv', 'w'))
f.writerow(['Company Name','Description', 'Person Name', 'Phone Number', 'EmailAddress','Web Address'])

dash = ["https://www.iomchamber.org.im/members/?Page=1&",
        "https://www.iomchamber.org.im/members/?Page=2&",
        "https://www.iomchamber.org.im/members/?Page=3&",
        "https://www.iomchamber.org.im/members/?Page=4&",
        "https://www.iomchamber.org.im/members/?Page=5&",
        "https://www.iomchamber.org.im/members/?Page=6&",
        "https://www.iomchamber.org.im/members/?Page=7&",
        "https://www.iomchamber.org.im/members/?Page=8&",
        "https://www.iomchamber.org.im/members/?Page=9&"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 comp = soup.select('div[class="members-list"] > div[class="standard-member"]')
 companysDatass = soup.select('nav[class="pagination"] ul > li > a')
for company in companysDatass:
     links = company.get('href')
     rr = requests.get(links)		# r variable has all the HTML code
     soups = BeautifulSoup(rr.content, 'html.parser')
     print(links)
for companyss in comp:
     for companyName in companyss.select('div[class="member-content"] > h3'):
         companyName = companyName.text 
     for description in companyss.select('div[class="member-content"] > p'):
         description = description.text
     for person in companyss.findChildren("i" , {'class': "fas fa-user"}):
         person = person.parent.text
     for telephone in companyss.findChildren("i" , {'class': "fa fa-phone"}):
         telephone = telephone.parent.text
     for email in companyss.findChildren("i" , {'class': "fa fa-envelope"}):
         email = email.parent.text
     for webaddress in companyss.findChildren("i" , {'class': "fa fa-desktop"}):
         webaddress = webaddress.parent.text
         info = [companyName,description, person, telephone,email,webaddress]
         print(info)
         f.writerow(info)   
         
 
