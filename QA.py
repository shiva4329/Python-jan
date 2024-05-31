x = [10,[20,30]]

print(x[1])

print(x[1][1])

print(x[-1])

x = [10,[20,30,[40,50]]]

print(x[1][2])


x = [10,20,('python')]

print(x[2][2])

x = (10,20,[30,{'name':'shiva'}])

print(x[2][1]['name'])

x = [10,20] + [30,40]
print(x)

x = (10,20) + (30,40)
print(x)

x = [10,20,30,40,50]
print((x[::-1]))



x = [10,20,'python',[({'car':'Ford'})],[30,40]]

# extract 'Ford'
print(x[3][0]['car'])


# extract 40
print(x[4][1])

# extract 'thon'
print(x[2][2:])

# print the x in reverse order
print(x[::-1])