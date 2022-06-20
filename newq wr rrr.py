import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('iom.csv', 'w'))
f.writerow(['Company Name','Description', 'Person Name', 'Phone Number', 'EmailAddress','Web Address'])

dash = ["https://www.iomchamber.org.im/members/?Page=1&"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 comp = soup.select('div[class="members-list"]')
for companyss in comp:
     for companyName in companyss.select('div[class="member-content"] > h3'):
         companyName = companyName.text 
         #print(companyName)
     for description in companyss.select('div[class="member-content"] > p'):
         description = description.text 
         print(description)
     for personName in companyss.select('a[class="contact-link no-contact-link"]'):
         personName = personName.text
         #print(personName)
         telephone = companyss.select('a[class="contact-link"]')
         telephone = telephone[1].text
         emailAddress = companyss.select('a[class="contact-link"]')
         emailAddress = emailAddress[2].text
         webAddress = companyss.select('a[class="contact-link"]')
         webAddress = webAddress[3].text
         info = [companyName,description,personName,telephone,emailAddress,webAddress]
         print(info)
         f.writerow(info)
   	   	
 
        

         
     
     
