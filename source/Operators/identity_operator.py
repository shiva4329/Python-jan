# identity operator
#               is      -----> compares the values address
#               is not  -----> compares the values address


# # memory adress ---> internally when we assign the value to variable system allocates the some address 
#                             to store the value in our local


# same values with diff variable ---> same address
x = 10
print(id(x))

y = 10
print(id(y))

# same variables with diff values ---> diff address
x = 10
print(id(x))

x = 20
print(id(x))

# diff variables with diff values ---> diff address
x = 10
print(id(x))

y = 20
print(id(y))


# list ----> mutable
#  same values with diff varibales ----> diff address
x = [10,20,30]
print(x,id(x))

y = [10,20,30]
print(y,id(y))

#  same values with same variables ----> diff address
x = [10,20,30]
print(x,id(x))

x = [10,20,30]
print(x,id(x))

#  diff values with diff variables ----> diff address
x = [10,20,30]
print(x,id(x))

y = [10,20,30,40,50]
print(y,id(y))

