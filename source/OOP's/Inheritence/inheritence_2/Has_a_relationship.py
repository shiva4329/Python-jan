# types of Inheritence : Is-a-relation in-heritence
#                        Has-a-relation


class A:
    def m1(self):
        print('Im m1 method')

class B(A): # Is.a.relation
    def m2(self):
        print('Im m2 method')



# b1 = B()
# b1.m1() # using ref variable/ object by calling the m1 method in class A




# has.a.relation
class A:
    def m1(self):
        print('Im m1 method')

class B: # Has.a.relation
    def m2(self):
        a1 = A() # calling A class
        a1.m1() # calling A method
        print('Im m2 method')



b1 = B()
b1.m2()# using ref variable/ object by calling the m1 method in class A