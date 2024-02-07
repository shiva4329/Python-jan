# print : it is an output function in python
# syntax ----> print()
#        3 types/ways :
#                       normal print : print()
#                       using f""   : print(f' ')/print(f" ")
#                       using .format : print(''.format())/print("".format())

# normal print

x = 100
y = 200

print(x,y)


# using f""

print(f"{x},{y}")



# using .format

print("{0},{1}".format(x,y))

a = 10
b = 20
c = 30

print("{0},{1},{2}".format(a,b,c))

print("{1},{0},{2}".format(a,b,c))

print("{2},{0},{2}".format(a,b,c))

print("{0},{2}".format(a,b,c))

print("{0},{1},{1}".format(b,c))



print(f"{a},{b}")

#print(f"{},{b}") # error bcoz place holder cant be empty

print(f'{b},{c}')




# using string : string is combination letters ---> using '..'," .... "


x = 'python'
y = 'hi'
z = 'hello'

print(x,y)

print(f'{x},{y}')

print('{0} {1}'.format(x,y))

print('{} {} {}'.format(x,y,z)) # by default it prints based on variables assigned in .format

#print('{} {} {}'.format(x,y)) # error bcoz 3rd values is not defined in .format

#print('{} {1} {0}'.format(x,y,z)) # error cannot use both cases

#print('{1} {0} {}'.format(x,y,z)) # error cannot use both cases

# example ----> 'python'

print(x)

print(f"'{x}'")

f'....'

f"...."

#### print(f''{x}'')

print(f'"{x}"')


# ---> hello i have 100 rupess

x = 100

print('hello i have 100 rupess')

print('hello i have '+str(x)+' rupess')

print(f'hello i have {x} rupess')

print('hello i have {0} rupess'.format(x))


