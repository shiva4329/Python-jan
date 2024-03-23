# create a fn with arguments, if parameter is not given while calling it shoult take it as zero

def sample(x=0,y=0): # default arguments(if we are not giving values while fn call it will take)
    print(x,y)

sample(20,30) # fn calling non-keyword arguments


# combination of keyword and non-keyword

def sample(x,y,z):
    print(x,y,z)

sample(10,z=20,y=30) # 10 is non-keyword, z,y : keyword


def sample(x,y,z): # non-default
    print(x,y,z)

sample(10,20,z=30) # 10 is non-keyword, z,y : keyword

# note : non-keyword arg follows keyword argument


#combination of default and non-default

def sample(x,y,z=0): # non-default and deafult
    print(x,y,z)

sample(10,20) # 10 is non-keyword, z,y : keyword

# note : non-default argument follows default argument