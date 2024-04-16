# two classes with same method name

# in this cases if method name is same : it ovwerites writes with latest method


class A:# child class
    def display(self):
        print('Im display method in A class')


class B(A):# parent class
    def display(self):
        print('Im display method in B class')



obj = B()
obj.display()


# note : if same method name in both class it will over-writes with parent class method

