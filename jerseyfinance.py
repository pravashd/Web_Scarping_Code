import requests
from bs4 import BeautifulSoup
import csv


dash = ["https://www.jerseyfinance.je/business-directory/#letter-A"]
for urls in dash:
 r = requests.get(urls)		# r variable has all the HTML code
 soup = BeautifulSoup(r.content, 'html.parser')
 print(soup.text)
