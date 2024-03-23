# create a list creation fn with n numbers n = real time input

# i/p = 5 , [0,1,2,3,4]

def list_fn(x=0): # default
    lis = [] # local variable
    if type(x) == int:
        for i in range(x):
            lis.append(i)
        print(lis)
        return lis
    else:
        print('x is not integer')

# x = 10  # global i/p varabile
# print(list_fn(x)) # non-keyword arg