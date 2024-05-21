
# create Company class
# define variables
#   Cname,Cadd,sal
# create options method
# create HRA method
#       sal = (sal*0.15) + sal
# create PF method
#       sal = (sal*0.12) - sal




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
            self.HRA()
            self.options()
        elif self.input == '3':
            print('PF deduction')
            self.PF()
            self.options()
        elif self.input == '4':
            print('Exit')
            exit()
        else:
            print('Invalid Options')


    def SalaryCheck(self):
        print('Employee Salary :',Company.salary)

    def HRA(self):
        print('HRA : ', Company.salary * 0.15)
        Company.salary = (Company.salary*0.15) + Company.salary
        print('Final Salary :', Company.salary)

    def PF(self):
        print('PF : ', Company.salary * 0.12)
        Company.salary = Company.salary - (Company.salary*0.12)
        print('Final Salary :', Company.salary)

e1 = Company()

e1.options()
