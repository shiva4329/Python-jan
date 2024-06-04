#
import pandas as pd
import numpy as np


# read the csv

df = pd.read_csv('/home/siva/Documents/python_jan_batch/Python-jan/pandas/train.csv')
print(df)


# only column extraction
print(df.columns)

# null value count
print(df.isnull().sum())

#replace null values with 0
df.fillna(0,inplace=True) # inplace is for saving/comming the changes into data

# null value count
print(df.isnull().sum())

# applying filter on saleprice column

data = df[(df['SalePrice']>150000) & (df['SaleCondition'] == 'Normal')]

print(data)

# create new column 'resale'

df['Resale'] = [1 for i in range(df.shape[0])]

print(df)

# create new column 'SaleDecide'
def decide(data):
    if (data> 150000):
        return 'Y'
    else:
        return 'N'

df['SaleDecide'] = df['SalePrice'].apply(decide)

print(df)