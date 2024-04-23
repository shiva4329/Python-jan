# we can globalize the local variable into global variable using? = 'global' keyword
# syntax : global <varaiable name>

#


# using global and local varaibles

x = 100 # global

def addition():
    global x # globalizing the variable
    x = 10 # local
    y = 20 # local
    print(x) # calling x variable in the fn


addition()

print(x) # calling x varaiable out side the fn