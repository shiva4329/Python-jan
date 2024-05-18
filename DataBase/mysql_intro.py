# DataBase : where we can store the data

# types : 2
#          1. relational database
#            type of data :   data is in table format(rows/columns)
#                  Ex. MySql
#          2. non-relational database
#               type of data :  document(dictionary)
#                  Ex. NoSQl(MongoDB)


# MySQl : it is one of the popular relational database

# datatypes:
#           int
#           varchar(255) ---> max length
#           varchar(20) ----> particular length---> 20 char




# Creating data base
#     create database <db name>;

# use the created database / particular data

#          use <db name>;

# check the available tables in database

#       show tables;

# create table in database

    #  create table <table name>(col1 dtype,col2 dtype......);


# inserting data into table

    #   insert into Student(id,name,age,address,mobile) values(1,'miller',34,'US','012345678');

# display  total data

    # select * from <table name>


# display data for particular column filter

    # select * from Student where age = 34 and address = 'US';

    # select * from Student where age > 30;

# display specific column data

    # select name from Student;

    # select name,age from Student;


# reset mysql-password

    #alter user 'user'@'localhost' identified by 'New password';