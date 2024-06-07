# steps to insert data from Excel/CSV file to MySQL


# read the file using pandas
# connect to the MySQL
# extract the columns from file
# create a table in MySQL using extracted coulumns from file
# read the row by row values from file and insert the data into MySQL



# code
# importing library's
import pandas as pd
import pymysql as pm


# reads the file
df = pd.read_excel('/home/siva/Desktop/student_details.xls')
print(df)

# connect to the mysql db
con = pm.connect(user = 'root', password= 'Root', host= 'localhost',db='School')
print(con)
cur = con.cursor() # creating cursor

# extracting the columns from file data
df_cols = []
for i in df.columns:# reading cols from df
    r = i.replace(' ','') #removes empty sp[ace from col name
    df_cols.append(f'{r} varchar(50)') # adding datatype for col name

x = ','.join(df_cols) #removes quote(') from string

# creating table using columns
# note : if table is already available in mySql no need run create command, if not only need to run create command
query = f"create table Students({x})" # generating table creation query
print(query)
cur.execute(query) # if table is not exist

# reading data from file row by row and inserting
for i,row in df.iterrows():
    row = [str(i) for i in list(row)] # extracting rows from file
    query = f'Insert into Students values{tuple(row)}'# generating insert query
    print(query)
    cur.execute(query) # executing insert command
    con.commit()# savinf data into MySQL