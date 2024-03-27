# file handling : creating files, inserting data, reading a file..........

# file handling can be done by using below fn's

# open() : when you are using this close() should be used at the end of the operation
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
#               r+ = read+wrigt - same as 'r' it will allows to write the data
#               w+ = read+wright - same as 'w' it will allows to read the data
#               a = append the data - if old data is exists it will just add the new data at the end
#               a+ = append+read



# how to create a file using open() and with

f1 = open('sample1.txt','w')
f1.close()


with open('sample2.txt','w') as f2:
    pass



