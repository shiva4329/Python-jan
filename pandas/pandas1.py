

# pandas : is on of the most powerful/popular/useful library for ML and DS
# for extracting data from files and also data cleanig operations

#
import pandas as pd


# read the csv/excel file using pandas /home/siva/Desktop/student_details.xls
data = pd.read_excel('/home/siva/Desktop/student_details.xls')
print(data)

# find the length of file
print(data.shape) # retuns the length of data in row/column format

# only row count
print(data.shape[0])

# only column count
print(data.shape[1])

#gives the detailed information about the numeric data column
print(data.describe())

#gives the detailed information about the columns
print(data.info())

# read the columns in file
print(data.columns)

# reads the particular row data
print(data.iloc[1])

# read the data row by row
# for i in data.iterrows():
#     print(i[1][3])

# particular column
print(data['First Name'])

# read the multiple column data ex: two columns
print(data[['First Name','Last Name']])

# reads the particular multiple data
print(data.iloc[:3])

# get the data based on filter on single column
filter_data = data[data['First Name']=='Philip']
print(filter_data)

# get the data based on filter on single column
filter_data = data[(data['First Name']=='Philip') & (data['Id']>100)]
print(filter_data)


# find the null count
print(data.isnull().sum())