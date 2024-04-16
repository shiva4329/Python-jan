# accessing both parent class and child class properties/values/variables

# child/sub-class
class A:
    a = 10 # static
    def m1(self):
        self.b = 20 # non-stat
        print('from m1 method ....')


# parent/super class
class B(A): # inheriting the A class prop
    c = 30 # stat
    def m2(self):
        self.d = 40 # non-stat
        print('from m2 method ....')



obj = B() # calling parent class, obj contains both class properties
obj.m1()
obj.m2()

print(B.a) # calling A class static variable
print(obj.b) # calling B class non-static variable

print(B.c) # calling B class static variable
print(obj.d) # calling B class non-static variable


# what is happening internally:

# when we create objects(obj) of class B, first it checks the class B is (extending)parent/super class or not,
# if it extends the first it creates the object of Class A , then it creates the object for Class B.

# both the objects () are stored in same memory




