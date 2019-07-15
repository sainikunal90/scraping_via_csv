from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np 


df = pd.read_csv(r'C:\Python\scraper\url_csv.csv',dtype='unicode')

df1 = df['url_key']
x = np.array(df1) 

for element in x:
    paytm_source = requests.get(element).text
    soup = BeautifulSoup(paytm_source, 'lxml')
    paytm_price = soup.find('span', class_ = '_1V3w').text
    print("Paytm Price:", paytm_price)
