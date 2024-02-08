# string fn/methods ---> 
#    len() --- length of string
#      type() ---> which type of data
#

# funtions

x = 'Good Morning'

#type()
print(type(x))

#len()
print(len(x))

# string methods

x = 'python'# original 

# upper()

print(x.upper())
y = x.upper()
print(x)
print(y)

# lower()
a = 'ABCD'
print(a.lower())

# captialize()
x = 'india'
print(x.capitalize())

# swapcase() ---> lower to upper /upper to lower

x = 'InDiA'
print(x.swapcase())

# startswith() ---> checks the string with 'char' retuns True/ false
x = 'India'
y = "India is my count"
print(x.startswith('I'))
print(x.startswith('A'))


# endswith() --> end value check
x = 'India'
y = "India is my country"
print(x.endswith('a'))
print(y.endswith('t'))
print(y.endswith('country'))
print(y.endswith('z'))

# strip() -- removes empty spaces starting of the string and ending of the string

x = '   good morning   '
print(x,len(x))
print(x.strip())

# lstrip() -- removes only starting empty spaces
print(x.lstrip(),len(x.lstrip()))

# rstrip() -- removes only ending empty spaces
print(x.rstrip(),len(x.rstrip()))
