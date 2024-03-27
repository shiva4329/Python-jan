# ##Task
#
# Create a folder named 'Avengers' With in that folder
# create a file 'output.txt'
#
# Using Os moudule and open() functions
#
# W.a.p to add two numbers take realtime inputs and Store the output into 'output.txt' file
#
# Sample:
#
# X = 10
# Y = 20
#
# Output:
#
# Write the output into 'output.txt' file as below format
#
# 'Sum of x and y is 20'


import os

def addition(x,y):

    return x+y


# z = addition(10,20)

# print(z)


# creating folder using os module

if 'Avengers' not in os.listdir(): # if folder is not available it will creates the folder else it wont create
    os.mkdir('Avengers') # it will creates the folder in current directory

print(os.listdir())

# creating output.txt using with

# syntax : with open(path,mode) as <variable>:
#                 .............with block.....

with open('Avengers/output.txt','a+') as file:
    z = addition(10,2000)
    file.write('\n'+str(z))

print(os.listdir())