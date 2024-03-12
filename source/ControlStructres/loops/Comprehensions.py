# comprehensions : single line format
# list : syntax : [<var> for-loop <conditions/expressions>]
# tuple
# set
# dict : syntax : {key:value for i in <variable/fn> <condition>}


ip = 10
lis = []

for i in range(1,ip+1):

    lis.append(i)

print(lis)

# list comprehension 

x = [i for i in range(1,ip+1)]

print(x)


# list comprehension with even numbers
x = [i for i in range(1,ip+1) if i%2 == 0]

print(x)


# tuple comprehension

vals = range(10)

y = (i for i in vals)

print('tuple : ',y)

# Note : tuple comprehension generates indirect object


# set comprehension
val = range(10)
a = {i for i in val }

print(a,type(a))


# dictionary comprehension : syntax : {key:value for i in <variable/fn> <condition>}

dictionary = {i:i for i in range(10)}

print(dictionary)

# create a dictionry using two lists

k = ['a','b','c']
v = [10,20,30]

print(zip(k,v)) # generates indirect object it holds : a,10,b,20,c,30

z = {i:j for i,j in zip(k,v)}
print(z)
