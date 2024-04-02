# creating sample prgram using oops
# syntax :

"""

class <class name>:
    def <method name>(self):
            pass

"""

# why we call method in class insted of fn's
# the fn' belongs to particular class that why we called its as method using by 'self' arg in method

class sample:# class creation
    def display(self): # method
        print('hello')
        print(self)

# sample().display() # method calling

x = sample() # calling a class and creating an object
print(x)
# x holds indirect address of sample() ---> we can use x as an calling object for methods
x.display()


y = sample()
print(y)
y.display()

