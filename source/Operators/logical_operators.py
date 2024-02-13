# logical operators
#           and --- if both are ture returns true else false
#           or  --- if any one is true returns true else false
#           not --- trues becomes false, false becomes true


# AND truth table

#       A       B       and
#   ----------------------------
#       T       T       T
#       T       F       F
#       F       T       F
#       F       F       F


# OR truth table

#       A       B       or
#   ----------------------------
#       T       T       T
#       T       F       T
#       F       T       T
#       F       F       F

# NOT truth table

#       A      not 
#   ----------------------------
#       T       F
#       F       T


# and

x = True
y = True

print(x and y)
print(x or y)

x = True
y = False

print(x and y)
print(x or y)

x = False
y = True

print(x and y)
print(x or y)

x = False
y = False

print(x and y)
print(x or y)


# in binary representation
# True = 1
# false = 0

x = 1
y = 0

print(x and y)
print(x or y)



# using if condition ---> 
# syntax :

#  if (condition/logic/expression):
#           .............
#           .............
#           .............



x = 15

# check x is even or not ----> divide by 2 returns reminder 0

if x%2 == 0 :
    print(x,x%2)

x = 9
y = 4

if (x%2 == 0) and (y%2 == 0): # f and t == f
    print(x,y)


x = 9
y = 4

if (x%2 == 0) or (y%2 == 0): # f or t == t
    print(x,y)


# not 

x = True
print(not x)

x = False
print(not x)


x = 1
print(not x)

x = 0
print(not x)


x = 10

if not (x%2 == 0): # not t = f
    print(x)


x = 7

if not (x%2 == 0): # not f = t
    print(x)

