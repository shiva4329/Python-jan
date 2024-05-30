



class HRA:
    def Hra(self,salary):
        print('HRA : ', salary * 0.15)
        salary = (salary*0.15) + salary
        print('Final Salary :', salary)
        return salary