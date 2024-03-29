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

except:
    print('error in try block check the logic')



try: # checks for the erors and gives to except
    print(100 / 1)
    # print(10 + 'a')
    f3 = open('blue.txt', 'r')

except ZeroDivisionError: # handles the particular exception
    print('error in try block check the logic')

except FileNotFoundError:
    print('file is missing, pls check')

except: # handles te all types of errors
    print('all')

finally: # finally will run not matter what ever the error (or) no error
    print('hello')
