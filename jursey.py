import requests
import pandas as pd

url = 'http://www.jersey.co.uk/finance/lawyers.html'
html = requests.get(url).content
df_list = pd.read_html(html)

df = df_list[-1]
print(df)
df.to_csv('finance-lawyer.csv')


   	
 
