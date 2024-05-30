#
# create 'Employee' table with Id,Name,Age,Salary
# insert 5 rows of data
# using python


# 1. mysql work bench

    # select database
    # use School;

    #  creating table
    # create table Employee(Id int,Name varchar(50),Salary varchar(50),Age varchar(3))
    #
    # display data
    # select * from Employee

    # inserting data into table
    # insert into Employee(Id,Name,Salary,Age) values(101,'sam','25000','28');

    # display data
    # select * from Employee



# 2. try with python

import pymysql


# connect to db
con = pymysql.connect(user='root',password='Root',host='localhost')

# creating cursor for writing Queries
cur = con.cursor()

# writing queries

# go into db
cur.execute('use School')

# show tables

cur.execute('show tables')
for i in cur:
    print(i)

# create Employee1 table
cur.execute('create table Employee1(Id int, Name varchar(50), Salary varchar(50), Age varchar(3))')

# show tables

cur.execute('show tables')
print(list(cur))

#
cur.execute('Insert into Employee1(Id int, Name, Salary, Age) values (101,"sravya","25000","28")')

# saving data into
con.commit()

# show data
cur.execute('Select * from Employee1')
print(list(cur))




# in SQL
# update query ---->
# drop table/delete

# what is join
# types of joins
# purpose of joins

#


