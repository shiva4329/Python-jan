# exception : error - it breaks the code
# syntax

# try:
#     ............................
#     ...........try block.................
#
# except:
#     ........except block............:


# print(100/0)

# print(10+'a')

# f3 = open('blue.txt','r')

try:
    print(100 / 0)
    print(10 + 'a')
    f3 = open('blue.txt', 'r')

except FileNotFoundError:
    print('error in try block check the logic')



try: # checks for the erors and gives to except
    print(100 / 1)
    # print(10 + 'a')
    f3 = open('blue.txt', 'r')

except ZeroDivisionError: # handles the particular exception
    print('error in try block check the logic')

except FileNotFoundError:
    print('file is missing, pls check')
except ZeroDivisionError: # handles the particular exception
    print('error in try block check the logic')

except FileNotFoundError:
    print('file is missing, pls check')

except: # handles te all types of errors
    print('all')

finally: # finally will run not matter what ever the error (or) no error
    print('hello')





# check the file is available or not using try.......excepe

try:
    f1 = open('sample1.txt','r')
    print(f1.read())

except FileNotFoundError:
    print('File is Missing')
    f1 = open('sample1.txt', 'w')
    f1.write('Welcome')

finally:
    f1.close()