# what is OS module = it provides the ways of interacting with Operating system like creating files, folders, and deleting folders and files
#                       like environment path settings



# methods in OS module :
#     getcwd() == gets the current directory
#     mkdir() = make directory(folder)
#     listdir() = list directory/ list of all files and folders in the directory
#     rmdir() = remove directory
#     remove() = remove file
#      rename() = renames the file or folder
import os # importing the OS module

# prints the current directory
print(os.getcwd())

# create a folder in current directory
# os.mkdir('/home/siva/Documents/python_jan_batch/Python-jan/source/Functions_1/Sample_test')

# rename the directory or file
# os.rename('/home/siva/Documents/python_jan_batch/Python-jan/source/Functions_1/Sample_test','/home/siva/Documents/python_jan_batch/Python-jan/source/Functions_1/Test_sample')

# list all the content in the currrent directory
print(os.listdir())

# create a file in currnt directory == open() / with

# open() = when we use the open fn we need to use close() fn also

# syntax : open(path,mode)

# modes :
#         r = only read
#         w = writes the data, if files is already exit remove the old data and writes the new data,
#             if file is not exits creats the file
#         a = appends the data with existing data
#         rb = read the binary data
#         wb = writes the binary mode

# open('teddy.txt','w')

# read the file

f = open('sample_1.txt','r')
print(f.read())

# writes the data

# note : if using 'w' mode truncates the existing data and over-writes the new data
f = open('sample_1.txt','w')
msg = 'Welcome to java'
f.write(msg)
# f.close()


# append the data with existing data
f = open('sample_1.txt','a')
msg = '\nWelcome to C++'
f.write(msg)