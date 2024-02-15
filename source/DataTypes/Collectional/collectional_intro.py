# collectional datypes : sequence of values
# types : 
#           list []
#           tuple ()
#           set {}
#           dictionary {key:value}

# list [] ---- 
#               list is mutable(changeable)
#               list follows index ---> forward,backward
#               list allows homogeneous(same types of values), hetro(diff types of values)

# list

x = []
print(x)
print(id(x)) # memory address of variable
print(len(x))
print(type(x))

# homo -- same datatype
x = [10,20,30,40,50]
print(x)
print(len(x))
print(id(x))
print(type(x))

# hetro -- diff datatype
x = [10,12.04,'hai',True,10+3j]
print(x)
print(len(x))
print(id(x))
print(type(x))

# indexing --->

x = [10,20,30,40]
print(x[2])
print(x[-3])

print(x[1:])
print(x[-4:-1])

# mutable ---> 
x = [10,20,30,40,50]
print(x)
x[3] = 35
print(x)
x[-1] = 500
print(x)
x[-1] = 50
print(x)



# operators --->

