# write an addition program using oops


class sample:
    def addition(self):
        x = 10
        y = 20
        z = x+y
        return z # return stores the value into method

print(sample().addition())



class sample:
    def addition(self):
        self.x = 10 # non-static variables
        self.y = 20 # non-static variables
        self.z = self.x + self.y
        return self.z # return stores the value into method
    # print(sample.x)
print(sample().addition())



class sample:
    x = 10 # static variables
    y = 20 #static variables
    def addition(self):
        z = sample.x + sample.y
        return z # return stores the value into method
print(sample().addition())




#

class sample:
    name = 'siva' # static variable
    def multiplication(self,x,y):
        self.z = x * y # non-static
        return self.z # return stores the value into method

obj = sample()
val = obj.multiplication(10,20)

print(f'value is {val}')
print(obj.name)
