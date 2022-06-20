import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('w-chamber.csv', 'w'))
f.writerow(['links','First Name','Last Name', 'Address', 'Phone Number','Fax', 'EmailAddress','WebAddress'])

dash = ["https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=50&sector&um_search=1",
        "https://www.iwchamber.co.uk/user/karenlucas/",
        "https://www.iwchamber.co.uk/user/carolinetaylor/",
        "https://www.iwchamber.co.uk/user/mrstevenharvey/",
        "https://www.iwchamber.co.uk/user/samscadgell/",
        "https://www.iwchamber.co.uk/user/kellyfenton/",
        "https://www.iwchamber.co.uk/user/roberthull/",
        "https://www.iwchamber.co.uk/user/kevinbarton/",
        "https://www.iwchamber.co.uk/user/charlesmoore/",
        "https://www.iwchamber.co.uk/user/maddydobson1/",
        "https://www.iwchamber.co.uk/user/salesteamidml-com/",
        "https://www.iwchamber.co.uk/user/andrewv/",
        "https://www.iwchamber.co.uk/user/mrscrossall/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysData = soup.select('div[class*="um-field-area"]')
 for company in companysData:
          print(company.text)
          for title in soup.select('div[class="listing-left"] > h1'):
            title = title.text
for address in soup.select('div[class="listing-left"] > p'):
        address = address.text
for phone in soup.select('div[class="listing-left"] > ul > li'):
        phone = phone.text.replace('\n','')
for point in soup.select('ul[class="feature-list"] > li'):
        point = point.text
for description in soup.select('div[class="more-about-us"]> p'):
        description = description.text
for description123 in soup.select('div[class="more-contact-item"]> p'):
        description123 = description123.text
info = [links,title, address, phone,description,description123]
print(info)
f.writerow(info)

info = [links,title, address, phone,description,description123]
print(info)
f.writerow(info)         