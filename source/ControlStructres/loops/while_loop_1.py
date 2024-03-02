# while loop : by default it is infinite loop, but we can make it as finite loop also as per our requiremnt
# it will iterates till condition satisfies if condition is FALSE 'while' will stops

# syntax :

# while <expression/comdition>:
#     ........................
#     ........................


#

#  infinite loop

# while True:
#     print('hello')

# finite loop
# only loops for 5 times

# loop = True
# counter = 0
# while loop:

#     print(counter,loop)
#     counter = counter + 1
#     if counter == 5:
#         loop = False
#         print(counter,loop)


# x = [10,20,30,40] # 4 -1 = 3

# loop = True
# counter = 0
# while loop:

#     print(x[counter],loop)
#     counter = counter + 1
#     if counter == len(x):
#         loop = False


x = "python" # 6 = 5+1

loop = True
counter = 0
while loop:

    print(x[counter],loop)
    counter = counter + 1
    if counter == len(x):
        loop = False