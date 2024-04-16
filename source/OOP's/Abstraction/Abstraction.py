# Abstraction : Hiding up the data and methods of a class
#   symbol : using double underscore '__' before the variable/method
#
# ex : properties of one class cannot be accessed by another class
#
# if a customer given to a bank class, then for 'n' no.of customers, only one class is created/used for that particular customer
#

# when we provided abstraction to variable/method we cannot call that outside the class bcoz
# it hides the variable/method so that we cannot use those outside the class
# but we can access inside the class


# hiding the static variable

class Employee:
    __ename = 'Miller' # static # provided abstraction
    eadd = 'US' # static

    def display(self):
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static



e1 = Employee()
e1.display()

# print(Employee.__ename)



# hiding the non-static variable

class Employee:
    __ename = 'Miller' # static # provided abstraction
    eadd = 'US' # static

    def display(self):
        self.__salary = 200000 # non-static # provided abstraction
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static
        print(f'Employee salary : {self.__salary}') # calling non-static



# e1 = Employee()
# e1.display()
#
# print(Employee.__ename)# cannot call outside the class
# print(e1.__salary) # cannot call outside the class



# hiding the method using abstraction

class Employee:
    __ename = 'Miller' # static # provided abstraction
    eadd = 'US' # static

    def __display(self): # providing abstraction to method
        self.__salary = 200000 # non-static # provided abstraction
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static
        print(f'Employee salary : {self.__salary}') # calling non-static

    def show(self): # for calling abstract method
        self.__display() # calling abstraction method

e1 = Employee()

# e1.display()  # cannot call outside the class

e1.show()

# e1.display()  # cannot call outside the class
# print(Employee.__ename)# cannot call outside the class
# print(e1.__salary) # cannot call outside the class