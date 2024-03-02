# loop : continous flow rotation
#
# types in loops : 2
#                       for loop - finite loop
#                       while loop - infinite loop

# for loop 
#       iterates over the sequence/ through sequence/ till the sequence

# syntax : 

    # for <assign var> in <variable>:
    #     .......................
    #     .......................



# range() : it will gives the range of number based on value given in it
# syntax : range(start,stop-1)

x = range(10) # by default if we give single value in it , it will consider starting from zero '0'
print(x)

x = range(1,10) # if we give two value in it , it will consider starting first values as starting value
print(x)

# unpacking the range() values using for loop
for i in range(10): # for loop iterates till range of values
    print(i)

for i in range(1,10+1): # for loop iterates till range of values
    print(i)

# note : when we are using for loop we need to use for only collection datatypes/ not for int,float,bool,complex

# for i in 10: # error bcoz int is not iterable
#     print(i)


x = [10,20,30,40]
# for i in len(x): # error bcoz int is not iterable,(len() returns int value)
#     print(i)

for i in range(len(x)): # range(len(x)) = range(4) = 0,1,2,3
    print(i)

# how to unpack values in x using for
    
for i in range(len(x)): # range(len(x)) = range(4) = 0,1,2,3
    print(x[i])