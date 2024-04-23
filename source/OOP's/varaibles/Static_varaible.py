# static varaiable : define with in the class not with-in the method
# non static : defines with-in-the method only using 'self'




# using both static variable and non-static variable


class A:
    x = 100 # SV
    def addition(self):
        self.x = 10 # NSV

        # inside SV and NSV calling
        print(A.x) # calling SV using Class name
        print(self.x) # calling NSV using 'self' name



obj = A()

#outside SV and NSV calling

print(A.x) # calling SV using Class name
obj.addition()
print(obj.x) # calling NSV using Class name


