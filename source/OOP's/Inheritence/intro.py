# In heritence - importing one class properties into another class

# sample in heritence using two classes

class A:
    def display(self):
        print('Im display fn in A class')



class B(A):# inheriting the A class properties into B class
    def show(self):
        print("Im show fn in B class")



obj = B()
obj.show() # calling B class method
obj.display() # calling A class method using B class object

