#combination of global, static, non-static

# global = outside the class/fn
# static = inside the class outside the method
# non-static = inside the method




x = 10 # global

class Company: # defining class

    x = 100 # static

    # print(x)

    def depart1(self): # defining method
        x = 1000 # local (x is global, but in this method we over-writing to 1000
        # so this 1000 value applicable only for this method)

        self.x = 2000 # non-static
        print(x)
        print(self.x)
        print(Company.x)
        print('Im department 1')

    # print(x)

# emp1 = Company()
# emp1.depart1()

# print(x) # global
#
# print(Company.x) # static
#
# print(emp1.x) # non-static





# overwriting-global value (apply changes to globally)

# when we want to update/overwrite the global variable
# value with-in the class/method need to use keyword 'global'
# syntax : global <variable name>

x = 10  # global


class Company:  # defining class

    global x # globalising the x variable
    x = 100  # static

    # print(x)

    def depart1(self):  # defining method

        global x  # globalising x variable

        x = 1000  # local

        self.x = 2000  # non-static
        # print(x)
        print('Im department 1')

    # print(x)


emp1 = Company()
emp1.depart1()

print(x)

# note : Here when using 'global' x will take the latest updated value