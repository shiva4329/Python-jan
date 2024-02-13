# operators ---> 
# types ----->  Arthmetic operators
#               Assignment operators
#               Comparision operator
#               Logical operators ---> AND truth table, OR truth able
#               Identity operators
#               Membership operators

# Arthmetic operators
#           + addition
#           - substraction
#           * multiplication
#           / division ---> returns quotient --> with decimal points -> 10.0                2)20(10
#           // floor division ---> returns quotient ---> with out decimal points ---> 10
#           % modulus ---> returns reminder
#           ** Exponential


# Assignment operators 
#               = assigining
#               += adding+assigning
#               -= sub+assigning
#               /= division+assigning
#               *= multi+assign
#               //=floor div+assign
#               %= modulus+assign
#               **=exponetial+assign

# Comparision operators
#               ==  equals to
#                > greater than
#                < less than
#               >= greater tha equals to
#               <= lessthan equsl to
#               != not equals to

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



# identity operator
#               is      -----> compares the values address
#               is not  -----> compares the values address


# # memory adress ---> internally when we assign the value to variable system allocates the some address 
#                             to store the value in our local


# same values with diff variable ---> same address
x = 10
print(id(x))

y = 10
print(id(y))

# same variables with diff values ---> diff address
x = 10
print(id(x))

x = 20
print(id(x))

# diff variables with diff values ---> diff address
x = 10
print(id(x))

y = 20
print(id(y))