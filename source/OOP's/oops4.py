# create a class for company and dep methods for
# diff employee object



# class creation for company
class company:

    name = 'HCL' # static
    addr = 'hyd' # static
    print('Company name', name)
    print('address ',addr)

    def dep1(self,val):
        # self.ename = input('Enter new emp name : ') # non-stat
        self.ename = val
        print(f'Employee name = {self.ename}') # calling non-stat


# calling for multiple employees

emp1 = company()
emp1.dep1('a')

emp2 = company()
emp2.dep1('b')

emp3 = company()
emp3.dep1('c')

# x = ['a','b','c','d','e']
# for i in range(5):
#     obj = company()
#     obj.dep1(x[i])

