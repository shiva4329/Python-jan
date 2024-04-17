#Multi-level Inheritence: Deriving a class from another derived class
class A:
    def m1(self):
        self.x = 10
        self.y = 20
        print('Im A method')

class B(A):
    def m2(self):
        self.a = 1.11
        self.b = 2.22
        print('Im B method')

class C(B):
    def m3(self):
        intsum = self.x + self.y
        print(intsum)
        floatsum = self.a + self.b
        print(floatsum)
        print('Im Derived method')



c1 = C()
c1.m1()
c1.m2()
c1.m3()

print(C.__bases__)
print(B.__bases__)




