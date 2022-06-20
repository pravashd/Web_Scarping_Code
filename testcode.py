import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://www.weareguernsey.com/business-directory/?qb=&cat=1000")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract first <h1>(...)</h1> text
first_h1 = soup.select('h1')[0].text
