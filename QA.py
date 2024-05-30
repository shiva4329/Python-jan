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