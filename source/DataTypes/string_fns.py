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

# count() ---> retunrs the occurens of letter

x = 'Good Morning'

print(x.count('o'))

# split() ---> split the values base on char

x = 'ram,sam'
print(x.split(','))

y = 'python'
print(y.split('t'))

z = 'ram,sam,rahil,miller'
print(len(z))
print(z.split(','))
print(type(z.split(',')))
a = z.split(',')
print(len(a))


# immutable ---> not changeable

a = 'python'
print(a[0])

#a[0] = 'j' # error bcoz str cant be changed, we cant override the original object

# replace() ---> it can replaces the value in string but stores in other varible
b = a.replace('p','j')
print(b)
print(a)
a = a.replace('p','j') # i we are using same varible with diff values in it holds the recent values
print(a)



# try it out

# 'Welcome to python, python is dynamically typed'

# extract 'dynamically' ---> by using forward index
# extract 'welcome' ---> by using backward index
# extract 'python is dynamically typed' ---> by using backward index

# count the 'python' occurences
# covert all to upper
# replace 'python' to 'java'
# split the string based on ',' and count the len values after split

x = 'python,java,c++'

x = 'python java c++'

x = 'Welcome to python, python is dynamically typed'

print(x.split(',')) # list dtype
print(len(x.split(',')))





