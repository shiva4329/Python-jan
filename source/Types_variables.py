# variables : to hold a value
# types: 4
#           Global : entire code(outside of fn/method)
#           Local : particular fn(inside fn)
#           Static :
#           Non-static :
#

# global : it can access in entire code(inside/outside the fn)
# local : it can access inside the fn


# global variable

x = 10 # global variable 
z = 50

# local

def sample(): # fn definition
    x = 100 # local variable
    y = 200
    print(x,y,z)

sample() # fn call
print(x)
print(z)



# both local and global variables

x = 100 # global
z = 50 # global

def sample():
    y = 200
    print(y)
    print(z) # accessing global variable inside fn with out define in local

sample()
print(x)
# print(y) # cannot access local varible ouside the fn


# modifying gobal variable with-in function

x = 100 # global
z = 50 # global

def sample():
    y = 200
    z = 500
    print(y)
    print(z) # accessing global variable inside fn with out define in local

sample()
print(x)
# print(y) # cannot access local varible ouside the fn
print(z)


# modifying gobal variable with-in function using 'gobal'

# global : it is used to modify the global value with-in function and gets the updated value ouside the fn

x = 100 # global
z = 50 # global

def sample():
    global z
    y = 200
    z = 500
    print(y)
    print(z) # accessing global variable inside fn with out define in local

sample()
print(x)
# print(y) # cannot access local varible ouside the fn
print(z)