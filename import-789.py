import requests
from bs4 import BeautifulSoup


url = "http://www.directory.im/cat_accountants/nc33862"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')
soup.findAll(attrs = {'class' : 'content'})
print(soup.prettify())




