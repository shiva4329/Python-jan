# Dictionary ----> dictionary is a combination key:value pay
#       syntax : {key:value,key_1:value_1,.........}
# features
#       it is mutable
#       it access values based on key
#       it allows duplicates, but dosent allow key duplicates, allows value
#       dictinary fn : dict()

#

student = {"name":"sravya",'id':258,'grade':'A+'}


print(student)
print(type(student))
print(len(student))

x = {1:"sravya",2:258,3:'A+'}

print(x)
print(type(x))
print(len(x))

# duplicates keys

x = {'a':10,'b':20,'c':30,'a':100,'c':50} # takes latest value

print(x)

# duplicates values

x = {'a':10,'b':20,'c':30,'d':10,'e':20} # allows duplicate values having diff keys

print(x)


# index
x = {'a':10,'b':20,'c':30,'d':10,'e':20}

# print(x[1]) # index dosent follow

print(x['b']) # single value

# print(x['a':'b']) # slicing dosent support

print(x['a'],x['b'])


# mutable -- using keys
student = {"name":"sravya",'id':258,'grade':'A+'}

print(student)

student['name'] = 'Ramya' # by changing values use keys

student['grade'] = 'o'

print(student)







