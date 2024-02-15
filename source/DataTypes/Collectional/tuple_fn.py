# tuple function/methods
#       function:
#           min()
#           max()
#           sorted() ----> it coverts into list and gives sorted list
#           reversed( ) ----> generates indirect address
#           del()

#       Methods:
#           .append() ---> x
#           .insert() ----> x
#           .pop() -----> x
#           .clear() -----> x
#           .extend() -----> x
#             + --------> x

x = (10,20,30,50,40,35)

# min()
print(min(x))

# max()
print(max(x))

# sorted()
print(sorted(x)) # sorted converts into list

# reversed()
print(reversed(x))

for i in reversed(x):
    print(i)
print(' ')
for i in reversed(sorted(x)):
    print(i)


# methods

x = (10,20,30,40)

# append()

# x.append(50) # dosent work in tuple

# insert()
# x.insert(1,15) # dosent work in tuple

# pop
# x.pop() # # dosent work in tuple

# clear()

# x.clear() # dosent work in tuple

# del
del(x) # delets entire tuple
# print(x)


# + ----> we can add two tuples using +
x = (10,20,30)
y = (40,50)
print(x+y)
z = x+y
print(z)


# extend()
# x.extend((100,200,300)) # dosent work
print(x)