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
# print(isbn.apply(lambda x: isbnlib.meta(str(x))))

metadata_list = []

for idx, i in enumerate(isbn.iloc[:10]):
    print(idx / len(df), end='\r')
    time.sleep(1)
    # try:
#         metadata = isbnlib.meta(i)
#         metadata.update(isbnlib.classify(i))

#         metadata_list.append(metadata)
#     except:
#         print(idx)
#         metadata_df = pd.DataFrame.from_dict(metadata_list)
#         metadata_df.to_csv('book_metadata.csv', index=False)


# df = pd.DataFrame.from_dict(metadata_list)
# print(df)