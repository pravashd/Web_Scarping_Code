import requests
from bs4 import BeautifulSoup
import csv

f = csv.writer(open('xyz-chamberr.csv', 'w'))
f.writerow(['First Name','Last Name', 'Address', 'Phone Number', 'EmailAddress','Web Address','About'])

dash = ["https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=1&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=2&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=3&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=4&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=5&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=6&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=7&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=8&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=9&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=10&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=11&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=12&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=13&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=14&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=15&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=16&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=17&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=18&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=19&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=20&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=21&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=22&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=23&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=24&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=25&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=26&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=27&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=28&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=29&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=30&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=31&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=32&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=33&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=34&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=35&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=36&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=37&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=38&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=39&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=40&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=41&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=42&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=43&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=44&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=45&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=46&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=47&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=48&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=49&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=50&sector&um_search=1",
         "https://www.iwchamber.co.uk/membership/members/?compnayname&members_page=51&sector&um_search=1"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 companysDatass = soup.select('div[class="um-member-name"] > a')
 for company in companysDatass:
     links = company.get('href')
     rr = requests.get(links)		# r variable has all the HTML code
     soups = BeautifulSoup(rr.content, 'html.parser')
     for firstName in soups.select('div[class="um-field um-field-first_name um-field-text um-field-type_text"] > div[class="um-field-area"]'):
         firstName = firstName.text 
     for lastName in soups.select('div[class="um-field um-field-last_name um-field-text um-field-type_text"] > div[class="um-field-area"]'):
         lastName = lastName.text 
     for address in soups.select('div[class="um-field um-field-address um-field-textarea um-field-type_textarea"]'):
         address = address.text 
     for phoneNumber in soups.select('div[class="um-field um-field-phone_number um-field-text um-field-type_text"] > div[class="um-field-area"]'):
         phoneNumber = phoneNumber.text 
     for emailAddress in soups.select('div[class="um-field um-field-user_email um-field-text um-field-type_text"] > div[class="um-field-area"]'):
         emailAddress = emailAddress.text 
     for webAddress in soups.select('div[class="um-field um-field-webaddress um-field-url um-field-type_url"] div[class="um-field-area"]'):
         webAddress = webAddress.text   
     for about in soups.select('div[class="um-field um-field-about um-field-textarea um-field-type_textarea"]'):
         about = about.text      
     info = [firstName,lastName,address,phoneNumber,emailAddress,webAddress,about]
     print(info)
     f.writerow(info)      