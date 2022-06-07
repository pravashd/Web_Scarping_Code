import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait  # for implicit and explict waits
from selenium.webdriver.chrome.options import Options  # for suppressing the browser
import csv


f = csv.writer(open('B2b-directory.csv', 'w'))
f.writerow(['Company Name','Description'])

option = webdriver.FirefoxOptions()
option.add_argument('headless')
driver = webdriver.Firefox()
# Making a GET request
driver.get('https://www.192.com/atoz/business/')
html = driver.page_source
# check status code for response received
# success code - 200
#soup = BeautifulSoup(html)
# Parsing the HTML
soup = BeautifulSoup(html)
print(soup)


dash = ["https://www.192.com/atoz/business/"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soups = BeautifulSoup(r.content, 'html.parser')		
 companysData123 = soups.select('ul[class="js-ont-people-atoz-surnames ont-atoz-column-list"] > li > a')
 for company12 in companysData123:
     links = company12.get("href")
     rr1 = requests.get(links)	
     soups789 = BeautifulSoup(rr1.content, 'html.parser')
     print(links)
