# varaibles are  two types : 1 - Global
#                              2 - local



# global variable - outside the code, can call it any where in the code
# local variable - can be defined with-in-the function can be called and use with-in the fn only




# using global and local varaibles

x = 100 # global

def addition():
    x = 10 # local
    y = 20 # local
    print(x) # calling x variable in the fn


addition()

print(x) # calling x varaiable out side the fn

