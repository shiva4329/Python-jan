# create a function with simple addition operation with two values

def addition():
    x = 10 # local
    y = 20 # local
    z = x+y # local

    print(f'sum of {x} and {y} is {z}')

addition()

# create a function with simple addition operation with two values

def addition():
    x = int(input('Enter x value : ')) # local
    y = int(input('Enter y value : ')) # local
    z = x+y # local
    print(f'sum of {x} and {y} is {z}')

addition()