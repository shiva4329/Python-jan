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


# write a program to print given i/p is vowel or not in any case(upper/lower)

# x = input("enter x value : ")

# if (x in 'aeiou') or (x in 'AEIOU'):
#     print(x, 'is vowel')

# elif (x not in 'AEIOU') or (x not in 'aeiou'):
#     print(x, 'is Consonent')


# Write a program to check students’ grades.  Your program should fulfill the following conditions:

# Take input variable as 'grade'

# Ex : grade = input()

# Grade A – Outstanding
# Grade B – Excellent
# Grade C – Very Good
# Grade D – Good
# Grade E – Satisfactory
# others – Unrecognized/failed
    

# grade = input('Enter student Grades: ')

# if grade.lower() == 'a':
#     print('outstanding')
# elif grade.lower() == 'b':
#     print('excellent')
# elif grade.lower() == 'c':
#     print('Very Good')
# elif grade.lower() == 'd':
#     print('Good')
# elif grade.lower() == 'e':
#     print('Satisfactory')
# else:
#     print('failed')

# if grade.lower() == 'a':
#     print('outstanding')
# if grade.lower() == 'b':
#     print('excellent')
# if grade.lower() == 'c':
#     print('Very Good')
# if grade.lower() == 'd':
#     print('Good')
# if grade.lower() == 'e':
#     print('Satisfactory')
# if grade.lower() in 'fghijklmnopqrstuvwxyz':
#     print('failed')


# Write a program which does the following

# Take input for two integer variables a & b
# If a is greater than b, print 'a is bigger than b'
# If a is less than b, print ' b is bigigger than a'

# a = int(input('Enter A value : '))
# b = int(input('Enter B value : '))

# if a > b:
#     print('a is bigger than b')
# elif b > a:
#     print('b is bigger than a')
# else:
#     print('a == b')


# w p t if given number is same as reversed or not

# x = int(input('Enter number : '))

# y = reversed(str(x))

# z = ''

# for i in y:
#     z = z+i

# print(z)

# print(x == int(z))




# write a programm to find a given input year is leap year or not

# yr = int(input('Enter a year: '))

# if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 ==0):
#     print('leap_year')


# yr = int(input('Enter a year: '))

# if (yr % 400 == 0) and (yr % 100 == 0):
#     print('leap_year')
# elif (yr % 4 == 0) and (yr % 100 != 0):
#     print('leap_year')
# else:
#     print('not leap year')




# tasks
    
# w.a.p to find factorial for number (realtime i/p)
     # 5 = 5*4*3*2*1 = 120

# n = int(input('Enter the value : '))
# f = 1

# for i in range(1,n+1):
#     f = f * i
# print(f'Factorial of {n} is : {f}')

    
# w.a.p to print fibonacci series i/p number of values
    # i/p = 5 : 0 1 1 2 3

# num = int(input('Enter the value : '))

# x = 0
# y = 1
# for i in range(num): 
#     print(x)
#     z = x+y
#     x = y
#     y = z


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