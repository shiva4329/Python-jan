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


