import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://www.weareguernsey.com/business-directory/?qb=&cat=1000")
soup = BeautifulSoup(page.text, 'html.parser')

# Extract first <p>(...)</p> text
first_h1 = soup.select('biz-detail-title')


# print the result
print(first_h1)
