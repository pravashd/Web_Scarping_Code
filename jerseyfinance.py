import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv


driver = webdriver.Firefox()
# Making a GET request
driver.get('https://www.jerseyfinance.je/business-directory/#letter-A')
html = driver.page_source
# check status code for response received
# success code - 200
soup = BeautifulSoup(html,  features="lxml")
# Parsing the HTML
#soup = BeautifulSoup(r.content, 'html.parser')
f = csv.writer(open('m-directory.csv', 'w'))
f.writerow(['Links','Title','Address','Telephone/Fax'])

driver = ["https://www.jerseyfinance.je/business-directory/#letter-A"]
for urls in driver:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 print(soup.text)
