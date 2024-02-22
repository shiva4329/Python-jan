# Type Casting ---> converting one datatype to another datatype
#       int -- int()
#       string -- str()
#       float --- float()
#       boolean --- bool()
#       complex --- complex()

#------------------------ diff datatype to String-------------------------------------------------
# int to string
x = 10
y = str(10)

print(y,type(y))

# float to string
x = 14.05
y =str(x)
print(y,type(y))

# bool to string

x = True
y = str(x)

print(y,type(y))

# complex to string

x = 10+12j

y = str(x)
print(y,type(y))

# --------------------------String to diff data type----------------------------------------------------
# string to int

x = 'python'

# y = int(x) # error cannot convert string to int

x = "10"
y = int(x)

print(y,type(y))

# string to float

x = '10.25'
y = float(x)

print(y,type(y))

# string to bool

x = ''
y = bool(x) # empty string allways be False else True

print(y,type(y))

# string to complex

x = '10+12j'
y = complex(x)

print(y,type(y))

x = '10'
y = complex(x)

print(y,type(y))

x = 'A'
# y = complex(x) # error bcoz value should not in alphabets

print(y,type(y))

#----------------------------int to diff datatypes--------------------------------------------------

# int to string
x = 10
y = str(x)

print(y,type(y))

# int to float

x = 10
y = float(x)

print(y,type(y))

# int to bool

x = 10
y = bool(x)

print(y,type(y))

# int to bool

x = 0
y = bool(x)

print(y,type(y))

# int to bool

x = 1
y = bool(x)

print(y,type(y))

# int to complex

x = 25
y = complex(x)

print(y,type(y))

#-----------------------diff datatype to int----------------------------------------------------------

# string to int

x = 'a'
# y = int(x) # error cannot convert alphabets to int

print(y,type(y))

x = '1'
y = int(x)

print(y,type(y))

# float to int

x = 12.35

y = int(x) # removes the decimal part
print(y,type(y))

# bool to int

x = True

y = int(x) # True = 1
print(y,type(y))

x = False

y = int(x) # False = 0
print(y,type(y))

# complex to int

x = 10+6j

# y = int(x) # error cannot convert
print(y,type(y))


# remaining will be continued later...........