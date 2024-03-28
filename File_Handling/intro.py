# file handling : creating files, inserting data, reading a file..........

# file handling can be done by using below fn's

# open() : when you are using open() must close the file using  close()
# syntax :
#             open(path,mode)

# with : it will automatically closes the file
# syntax : with open(path,mode) as <variable>:
#                 .............with block.....


# file modes
#               r = read only - reads the file data
#               w = writes the data - if file not exists it will create the file and write the data
#                                       else it will write the data
#                                      note : it will delete the old data replaces with new data
#               r+ = read+write - same as 'r' and it will allows to write the data
#               w+ = read+write - same as 'w' and it will allows to read the data
#               a = append the data - if old data is exists it will just add the new data at the end
#               a+ = append+read



# how to create a file using open() and with

f1 = open('sample1.txt','w')
f1.close()


with open('sample2.txt','w') as f2:
        pass




# read the data in file
f1 = open('sample1.txt','r')
data = f1.read() # reads the data in file
print(data)
f1.close() # close the file

with open('sample2.txt', 'r') as f2:
    data = f2.read() # reads the file


# write the data in file
f1 = open('sample1.txt','w')
data = f1.write('hello') # reads the data in file
print(data)
f1.close() # close the file

with open('sample2.txt', 'w') as f2:
    data = f2.write('welcome') # reads the file


# append the data in file
f1 = open('sample1.txt','a')
data = f1.write('hello') # reads the data in file
print(data)
f1.close() # close the file

with open('sample2.txt', 'a') as f2:
    data = f2.write('welcome') # reads the file