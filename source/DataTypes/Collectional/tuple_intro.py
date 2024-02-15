# tuple () 

#   tuple is immutable(unchangebale)
#   tuple follows index
#   tuple allows duplicates
#   tuple allows homogeneous(same types of values), hetro(diff types of values)


x = ()
print(x,type(x))

y = 10,20,30,50,'python' # by default it will takes as tuple
print(y,type(y))

x = (10,20,'python',12.01,True)
print(x,type(x))


# allows duplicates
x = (10,10,10,20,30)
print(x)

# index

x = (10,20,30,40)
print(x[1:3])
print(x[-3:-1]) # -1-1 = -2

# immuatble

x = (10,20,30,40)

# change 30 to 300

# x[2] = 300 # tuple dosent allow item chnages

print(x)

y = [10,20,30,40]

y[2] = 300 # list dosent allow item chnages

print(y)




# memory address

# diff variable with same data ---> same address
x = (10,20,30)
print(x,id(x))

y = (10,20,30)
print(y,id(y))

# diff variable with diff data ---> diff address
x = (10,20,30)
print(x,id(x))

y = (10,20,30,40,50,60)
print(y,id(y))

# same variable with diff data ---> diff address
x = (10,20,30)
print(x,id(x))

x = (10,20,30,40,50,60)
print(x,id(x))