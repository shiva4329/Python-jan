# write a program for calculator using oops for passing two numbers



class calculator:

    def addition(self,x,y):
        print(f"sum of {x} + {y} is {x+y}")

    def substraction(self,x,y):
        print(f"diff of {x} - {y} is {x-y}")

    def multiplication(self,x,y):
        print(f"product of {x} * {y} is {x*y}")

    def division(self,x,y):
        print(f"result of {x} / {y} is {x/y}")





c1 = calculator()

# x = int(input("Enter x value : "))
# ip = input('Enter operation name : ')
# y = int(input("Enter y value : "))

x , ip , y= int(input()), input(), int(input())
# ip = input('Enter operation name : ')
# y = int(input("Enter y value : "))


print('----------------------')

if ip == "+":
    c1.addition(x,y)

elif ip == "-":
    c1.substraction(x, y)

elif ip == "*":
    c1.multiplication(x, y)

elif ip == "/":
    c1.division(x, y)

else:

    print('no such operation available')



print('-------------------------')


c2 = calculator()
c2.multiplication(4,2)
