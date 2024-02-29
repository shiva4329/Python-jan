# if ---
# syntax ----> 
'''
if <condition/expression>:
    ..............
    ....block.....
    ..............

'''

x = 10

if x == 100:
    print('value is matched')


x = 10

if x != 100:
    print('value is not matched')


x = 'Python'

if 'P' in x:
    print('value is present in ',x)


x = 'Python'

if 'x' in x:
    print('value is present in ',x)

x = 'Python'

if 'x' not in x:
    print('value is not present in ',x)




# check given number is even or not but input is real-time

x = 10

if x%2 == 0:
    print(x,'is even')


# real time

# x = int(input('Enter x input : ')) # input() -- default it will take as string

# if x%2 == 0:
#     print(x,'is even')

x = int(input('Enter x input : ')) # input() -- default it will take as string

if x%2 != 0:
    print(x,'is odd')

# using real time input ---> checheck the input is VOWEL or not
    # x is a 'VOWEL'


# write a program to check given i/p is alphabet or numeric
# write a program to print given i/p is vowel or not in any case(upper/lower)
# write a program to check given i/p is armstrong number or not


# 153 = 1*1*1 + 5*5*5 + 3*3*3 == > 1 + 125 + 27 ---> 153

# x = 256

# x_str = str(x)

# x_len = len(x_str)

# y = 0

# for i in x_str:
# #     print(i,int(i)**(x_len),type(i))
#     r = int(i)**(x_len)
#     y = y+r
#     print(y)

# if x==y:
#     print(True)





