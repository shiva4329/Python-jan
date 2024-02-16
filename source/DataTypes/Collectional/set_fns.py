# set functions/Methods
#       function:
#               min
#               max
#               sorted()


x = {10,20,30,40,15}

print(min(x))

print(max(x))

print(sorted(x))

# print(reversed(x)) #   dosent work in set

print(reversed(sorted(x)))




# methods:
        # add() ---> add item into list
        # clear() ----> clears the items in set
        # pop() -----> removes an item randomly
        # remove() ----> removes specifc item
        # union() ------> 
        # intersection ----> 


# add()

x = {10,20,30,40}

x.add(50)

print(x)

# pop()

x = {10,20,30,40}
print(x)
x.pop()
print(x)


# remove()

x = {10,20,30,40}
print(x)
x.remove(30)
print(x)

# clear()

x = {10,20,30,40}
print(x)
x.clear()
print(x)


# union

x = {10,20,30,40}
y = {30,40,50,60}

z = x.union(y) #  x U y ----> retuns all the items and with-out duplicates

print(z)


# intersection ----> returns common values

x = {10,20,30,40}
y = {30,40,50,60}

z = x.intersection(y)

print(z)

# difference
x = {10,20,30,40}
y = {30,40,50,60}

z = x.difference(y)
a = y.difference(x)

print(z)
print(a)

