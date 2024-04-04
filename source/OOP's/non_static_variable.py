# non - static varables :    declared with-in the method using 'self'
#                       not with-in the class
#                       accessed by using 'self' keyword inside the class
#                       can be accessed outside by using object name





class school:

    name = 'oxford' # static
    addr = 'hyd' # static

    print(name)
    print(addr)

    def section1(self):
        self.name = '1st class' # non-static
        self.strength = 60 # non -static

        print(self.name)
        print(self.strength)

    def section2(self):
        self.name = '2nd class' # non-static
        self.strength = 40 # non -static

        print(self.name)
        print(self.strength)

# school().section1()

std1 = school()

std1.section1()
print(std1.name) # calling non-static outside the class with obj name after calling method

# std2 = school()
# std2.section2()

