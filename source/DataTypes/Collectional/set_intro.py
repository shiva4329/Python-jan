# set() ---- {}

#               set is a  mutable
#               set does not allow duplicates
#               set doesnot follow index
#               set allows homo and hetro values
#               set fn ---> set()


x = {}
print(x,type(x)) # empty {} indicates dictionary

x = set()
print(x,type(x))


x = {10,20,30,40}
print(x)
print(len(x))
print(id(x))
print(type(x))

# hetro
x = {10,20,30,40,12.36,True,'hello'}
print(x)
print(len(x))
print(id(x))
print(type(x))

# duplicates ----> set does not allow duplicates

x = {10,20,30,40,10,20}
print(x)

# index ----> set does not follow index
x = {10,20,30,40}

# print(x[1]) #---> error bcoz set dont have index
