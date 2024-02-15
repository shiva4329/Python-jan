# string ---> combintion of letters
#    using single quots/double quots ---> '....', "...."
#     Example : 'python',"python"

# features of string in python
#               string is an immutable(un-changebale)
#               string follows index --- 2 types
#                                   forward -> left to right -> 0
#                                   backward -> right to left -> -1

# string

x = 'Python'
y = 'A'
z = "a"

print(x,type(x))

# string --- index

x = 'python'

# len()
print(x,len(x))

# forward index --> left - right --> 0
x = 'python'
# python -- 0,1,2,3,4,5
print(x[1])
print(x[4])
print(x[2])
print(x[5])

# slicing ---> extracting single letter/ some part of that string

x = 'python'

# 'pyt'
print(x[0:2]) # [lower bound:upper bound] --> allways upper bound -1
# [0:2-1] --> [0:1]

print(x[0:3])
print(x[0:5])


y = 'python is easy to understand.........'


# 'is .................'

print(y[7:]) # empty bound is infinite .i.e what ever the end value it will print till end

print(len(y))
print(y[:20]) # empty in lower bound is prints from starting

print(y[:]) # it will return complete string

# 
z = '666 ..... python java cobol sql.............'

print(z[7:])

print(z[:20])

print(z[:]) 
print(z)


# backward,string fn,string methods




