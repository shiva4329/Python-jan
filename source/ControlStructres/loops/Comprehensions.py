# comprehensions : single line format
# list : syntax : [<var> for-loop <conditions/expressions>]
# tuple
# set
# dict


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