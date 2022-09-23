import isbnlib
import pandas as pd
import time

df = pd.read_csv('data/books.csv',
                 quotechar='"',
                 usecols=['isbn'],
                 dtype={'isbn': str},
                 nrows=500,
                 )
isbn = df['isbn']

metadata_list = []

for idx, i in enumerate(isbn.iloc[:10]):
    print(idx / len(df), end='\r')
    time.sleep(1)
