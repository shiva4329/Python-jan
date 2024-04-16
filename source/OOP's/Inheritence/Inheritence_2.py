# create two classes with diff methods




class A:

    def addition(self):
        self.x = 10
        self.y = 20
        print(self.x+self.y)

    def subsraction(self):
        self.x = 10
        self.y = 20
        print(self.x-self.y)



class B(A):
    def mul(self):
        self.x = 10
        self.y = 2
        print(self.x * self.y)

    def div(self):
        self.x = 10
        self.y = 2
        print(self.x // self.y)


# calling substraction

# obj = A()
# obj.subsraction()

obj = B()
obj.div()
obj.addition()