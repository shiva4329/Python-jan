# static varables :    declared in inside class
#                       not with-in the method
#                       accessed by using class name
#                       can be accessed inside/outside by using class name



class school:

    name = 'Sri chaitanya' # static
    address = 'Hyd' # static

    print(name) # calling static in class
    print(address) # calling ststic in calss

    def section1(self):# method with-out logic

        print('In Method')
        print(school.name)
        print(school.address)



x = school() # calling school class
x.section1()


class school:

    x = 10 # static

    print(x)  # calling static in class
    print(id(x))

    def section1(self):  # method with-out logic
        self.x = 100 # non- static
        self.y = 150 # non-static
        print('In Method')
        print(x)
        # print(id(x))
        print(school.x)

    def section2(self):
        x = 1000 # non- static

        print(self.y) # calling non-static var from another method
        print('In Method')
        print(x)
        print(id(x))


obj = school()  # calling school class
obj.section1()
obj.section2()

# how to call ststic outside the class
# ans : using with class name
print(school.x) # class name

# how to call ststic outside the class
# ans : using with class name reference(object name)
print(obj.y) # with obj name

