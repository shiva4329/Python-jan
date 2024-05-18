# how to connect MySql from python ---> using pymysql library
# pre-req --> user,pwd,host name

# how to install lib

# syntax -- pip install <lib/package name>


# imports pymysql functionalities into python code
import pymysql


# creating connection with mysql using connect method

con = pymysql.connect(user='root',password='Root',host='localhost')

print(con)

# how to execute sql commands in python

# creating cursor
cur = con.cursor()

# command execution
cur.execute('use School;')

# show tables in database
cur.execute('show tables;')

for i in cur:
    print(i)

# get the total data from Student
cur.execute('select * from Student;')
print(cur)

for i in cur:
    print(i)
