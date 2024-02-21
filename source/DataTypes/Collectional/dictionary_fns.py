# dictonary functions/methods

# function
#       len() -- length of value
#       min() -- return minimum key
#       max() -- return maximum key
#       sorted() --- sorts only keys
#       reversed() --- reversed only keys

# min
x = {'a':10,'b':20,'c':30}

print(min(x)) # return minimum key

# max
x = {'a':10,'b':20,'c':30}

print(max(x)) # return maximum key

# sorted()
x = {'a':10,'c':20,'b':30}
print(sorted(x)) # sorts only keys

# reversed()
x = {'a':10,'c':20,'b':30}
print(reversed(x)) # reversed only keys

for i in reversed(x):
    print(i)


# methods
#           items() --- returns list of items in dict --> 1 item = 1 key:value
#           get() --- access the values based on key
#           keys() --- extracts only keys
#           values() --- extracts only values
#           update() ----- updates the dictionary
    
# items 

x = {'a':10,'b':20,'c':30}

print(x.items())

# get()

x = {'a':10,'b':20,'c':30}

print(x.get('b'))

# get()

x = {'a':10,'b':20,'c':30}

print(x.get('b'))

# values()

x = {'a':10,'b':20,'c':30}

print(x.values())

# how to add new key:value pair

x = {'a':10,'b':20,'c':30}

# add d=40

x['d'] = 40

# update() -- for extending the dict

x.update({'e':50,'f':60})

print(x)


# pop() -- removes value based on key

x = {'a':10,'b':20,'c':30}

x.pop('b')

print(x)

# remove() -- dosent work in dict

# clear()

x.clear() #-- clears items in dict
print(x)


# del()
x = {'a':10,'b':20,'c':30}
del(x) #-- delets entire dict
print(x)



# how intepreter works
# compare with compiler

# type casting 

# conditions/loops
# fns
# modules
# oops
# numpy
# pandas
# databse
# django

# ATM ---> check bal, deposit, withdra, final --- fn
#  oops

# exel ---> db ---> sql



