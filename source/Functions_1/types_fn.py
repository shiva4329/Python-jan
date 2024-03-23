# types of functions 4
#               default        -- fn def
#               non-default    --- fn def

#               keyword         -- fn call
#               non-keyword     -- fn call

# function with parameters

def addition(x,y): # fn def, non-default params/args
    print(x,y)

# addition(10,30) # fn call, non-keyword args

# keyword args

def display(x,y): # fn def, non-default params/args
    print(x,y)

# display(y=10,x=30) # fn call, keyword args


# keyword args

def display(x,y): # fn def, non-default params/args
    print(x,y)

# display(y=10,x=30) # fn call, keyword args

# default args/parms

def display(x=0,y=0): # deafult args
    print(x,y)

display(x = 50) # if we are not passing any values in fn call it will take default values assigned in fn def