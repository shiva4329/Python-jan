# return = saves the data into fn
# print() = just prints the data

# fn with print() -- it returns None into variable

def display(x):
    print(x)

x = 10
print(display(x))


# fn with return -- it returns None into variable

def display(x):
    print(x)
    return x # last of the with in function

x = 10
print(display(x))


# fn with return -- it returns None into variable

def display(x,y):
    z = x+y
    return z # last of the with in function

x = 10
y = 20
print('return',display(x,y))



# 
def display(x,y):
    z = x+y
    return z # last of the with in function

x = 10
y = 20
print('return',display(x,y))



a = 100

b = a + display(x,y) # 100 + 30

print(b)