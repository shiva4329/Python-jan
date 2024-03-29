#

# step 1: create a file input.txt using open/with
# step2 : create a logic/fn
#     take realtime data for x,y
#       x = input()
#
# step3 :write x,y 'input.txt'

# step3: read the data from input.txt
# step4 : split the data with split()

            # data = '10,20'
            #
            # x,y = data.split(',')
            #
            # print(x,y)

# step 5: perform addition operation
# step 6 : create output.txt file and write the data into output.txt




# file creation

# f1 = open('input1.txt','w')

# # realtime i/p
# x = input("Enter x value ")
# y = input("Enter y value ")
#
# z = f'{x},{y}'
# print(z)
# # write to file
# f1.write(z)
# f1.close()


# read data from input.txt

f1 = open('input1.txt','r')

data = f1.read()

print(data)

x,y = data.split(',')

sum1 = int(x)+int(y)

print(sum1)

f2 = open('output.txt','a')
f2.write(str(sum1))


# write a logic for if a file exists in the folder

# sample:
#         "input.txt"

import os

# listdir() == lists all the files/folders in the path

print(os.listdir())

if 'output3.txt' in os.listdir():
    f3 = open('output3.txt','r')
else:
    print(False)
    f3 = open('output3.txt', 'w')

# f3 = open('output3.txt','r')
