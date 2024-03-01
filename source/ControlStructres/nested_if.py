# nested if : if with in if
# syntax    :  

# if <expresssion/condition>:
#     .....................
#     ......................
#     if <expresssion/condition>:
#         ......................
#         .....................
#         if <expresssion/condition>:
#             ......................
#             ................
#         else:
#             ...........
#     else:
#         .................
# else:
#     ...................


# x = 'java'

# if x != '':
#     print('x is not empty')
#     if ('p' in x) or ('P' in x):
#         print('p is in x')
#         if x == x.lower():
#             print(x.upper())
#         else:
#             print('x is not lower')
#     else:
#         print('p not in x')
# else:
#     print('x is empty')


x = 'Python' # word case

if x != '':# checks value is empty or not
    print('x is not empty')
    if ('p' in x) or ('P' in x): # checks p is vailable or not
        print('p is in x')
        if x == x.lower(): # checking for lower 'python'
            print(x.upper())

        elif x == x.upper(): # checking for upper
            print(x.lower())
        elif x == x.capitalize():
            print('x is capitalize')
    else:
        print('p not in x')
else:
    print('x is empty')