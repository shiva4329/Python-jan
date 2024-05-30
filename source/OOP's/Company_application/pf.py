



class PF:
    def pf(self,salary):
        print('PF : ', salary * 0.12)
        salary = salary - (salary*0.12)
        print('Final Salary :', salary)
        return salary