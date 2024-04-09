# Abstarction : Hiding up the data and methods of a class
#   symbol : using double underscore '__' before the variable/method
#
# ex : properties of one class cannot be accessed by another class
#
# if a customer given to a bank class, then for 'n' no.of customers, only one class is created/used for that partcular customer
#

# when we provided abstration to varaiable/method we cannot call that outside the class bcoz
# it hides the variable/method so that we cannot use those ouside the class
# but we can access iside the class


# hiding the static varaible

class Employee:
    __ename = 'Miller' # static # provided abstartion
    eadd = 'US' # static

    def display(self):
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static



e1 = Employee()
e1.display()

# print(Employee.__ename)



# hiding the non-static varaible

class Employee:
    __ename = 'Miller' # static # provided abstartion
    eadd = 'US' # static

    def display(self):
        self.__salary = 200000 # non-static # provided abstartion
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static
        print(f'Employee salary : {self.__salary}') # calling non-static



# e1 = Employee()
# e1.display()
#
# print(Employee.__ename)# cannot call outside the class
# print(e1.__salary) # cannot call outside the class



# hiding the method using abstarction

class Employee:
    __ename = 'Miller' # static # provided abstartion
    eadd = 'US' # static

    def __display(self): # providing abstraction to method
        self.__salary = 200000 # non-static # provided abstartion
        print(f'Employee name : {Employee.__ename}') # calling static
        print(f'Employee address : {Employee.eadd}') # calling static
        print(f'Employee salary : {self.__salary}') # calling non-static

    def show(self): # for calling abstract method
        self.__display() # calling abstatction method

e1 = Employee()

# e1.display()  # cannot call outside the class

e1.show()

# e1.display()  # cannot call outside the class
# print(Employee.__ename)# cannot call outside the class
# print(e1.__salary) # cannot call outside the class