# what is a Function : to perform specific task
#                  a block of code that performs a specific task

# syntax : 

# def <fn name>(args1,arg2,....):
#     .........................................
#     .........fn block/ block of stmts.........
#     ..........................................
#     ...........................................

# create a simple addition function

def addition(): # fn creation
    x = 10
    y = 20
    print(x+y)


addition() # fn call


# create a simple Login function with realtime i/p


def Login(): # fn creation
    x = input('Enter User ID : ')
    y = input('Enter PWD: ')
    print('User Name :',x)
    print('password :',y)


Login() # fn call