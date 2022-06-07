import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
driver = webdriver.Chrome()
# Making a GET request
driver.get('https://www.192.com/atoz/business/')
html = driver.page_source
# check status code for response received
# success code - 200
soup = BeautifulSoup(html)
#Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup)

