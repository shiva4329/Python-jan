# list functions/methods

x = [10,20,30,40]

# append(value)

x.append(50) # appends the value at last position
print(x)

# insert(position,value) --> inserts value at particular position

x.insert(1,15)
print(x)

# pop()

x.pop() # delets the last value
print(x)

x.pop(1) # delets index/position value
print(x)

# remove(value) --> remove particular value
x.remove(30)

print(x)

# clear() ---> removes all items in list

x.clear()

print(x)


# del(variable) ---> removes entire list

# del(x) --- removes entire list

print(x)

# extend(list)

x = [10,20]

x.extend([30,40,50,60,'python'])

print(x)

# + 
x = [10,20]
y = [30,40]

z = x+y
print(z)


# functions()

# sorted() # sorts the list

x = [20,10,5,30]

print(sorted(x))

# min() gives minimum value

print(min(x))

# max() gives maximum value

print(max(x))

# reversed() ---> reverse the list

print(reversed(x))

for a in reversed(x):
    print(a)

print(reversed(sorted(x)))

for i in reversed(sorted(x)):
    print(i)

y = [i for i in reversed(sorted(x))]
print(y)


# reversed

x = [1,3,5,2,4]
print(x)

y = sorted(x) #ascending

print(y)

z = reversed(y)

print(z)

# append
a = []
for i in z:
    print(i)
    a.append(i)
print(a)