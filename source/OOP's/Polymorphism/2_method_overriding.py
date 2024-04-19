# method overriding : the method with same name and same no of parameters in both super class and
# sub class is known as over-riding


#

class A: # super class
    def m1(self):
        print('hello')


class B(A): # sub class
    def m1(self):
        print('hai')



y = B()
y.m1()# here subclass method is called or executed because super class method is overriden

# how to call super class method ?
# need to create seperate object for super class the we can call the super class method
x = A()
x.m1()
