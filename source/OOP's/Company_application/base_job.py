
from hra import HRA
from pf import PF



class Company:
    Cname = 'TCS'
    Cadd = 'HYD'

    salary = int(input('Enter Salary : ')) # SV

    def options(self):
        self.opts = '1 Salary 2 HRA 3 PF 4 EXIT'
        self.input = input("Enter options : ")

        if self.input == '1':
            print('Salary check')
            self.SalaryCheck()
            self.options()
        elif self.input == '2':
            print('HRA addition')
            Company.salary = HRA().Hra(Company.salary)# import from another file
            self.options()
        elif self.input == '3':
            print('PF deduction')
            Company.salary = PF().pf(Company.salary)# import from another file
            self.options()
        elif self.input == '4':
            print('Exit')
            exit()
        else:
            print('Invalid Options')


e1 = Company()
e1.options()