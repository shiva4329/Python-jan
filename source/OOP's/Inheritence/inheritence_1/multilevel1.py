#Multiple Inheritence : One derived class with multiple base classes

#Performing int sum,float sum,bool sum  in derived class by taking features from
#multiple base classes


class A:
    msg = 'Im A class' # static
    def m1(self):
        self.x = 10 # non-static
        self.y = 20 # non-static
        print('Im A method')

class B:
    def m2(self):
        self.a = 1.11
        self.b = 5.11
        print('Im B method')

class C:
    def m3(self):
        self.t = True
        self.f = False
        print('Im B method')


class D(B,A,C): # derived class with 3 bases classes
    def m4(self):
        intsum = self.x + self.y
        print(intsum)
        floatsum = self.a + self.b
        print(floatsum)
        boolsum = self.t + self.f
        print(boolsum)
        print(A.msg)
        print('Im derived class method')



c1 = D()
c1.m1()
c1.m2()
c1.m3()
c1.m4()

print(D.__base__)

print(A.__base__)