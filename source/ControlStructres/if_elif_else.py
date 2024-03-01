# suntax of if..elif..else

# if if condtion is true it dosent go to the elif
# if if is not satisfied will go to elif condition



# differe b/w (single if with multiple elif's (if...elif..elif..)) and (miltiple if's (if..if..) )

# if we use elif's : its breaks the flow when satisfies the condion/expression (recommened)
# if we use the multiple if's : it will checks all the if conditions and retunrs the o/p, some times we will face issues using this


# if <expression/condition>:
#     .........
# elif <expression/condition>:
#     .............
# else:
#     .........



x = [30,40]

if 10 in x:
    print('10 is in x')
elif 20 in x:
    print('20 is in x')
elif 100 in x:
    print('100 in x')
else:
    print('not statisfied above condi')


# x = [20,30,40]

# if 10 in x:
#     print('10 is in x')
# if 20 in x:
#     print('20 is in x')
# if 100 in x:
#     print('100 in x')
# else:
#     print('not statisfied above condi')