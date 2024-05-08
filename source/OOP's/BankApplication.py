# write a python for bank application using OOP's


# class creation
# declaring variables
# creating method for login
# creating method for deposit, withdrawl ,balance


#

class Bank:
    bank_name = 'HDFC' # SV
    bank_add = 'Sathupalli' # SV

    print(f'Bank Name : {bank_name}')
    print(f'Bank Branch : {bank_add}')

    bal = 0 # SV

    def __init__(self):
        self.user = input("Enter user name: ") # NSV
        self.password = input("Enter password : ") # NSV

        if (self.user == 'ABC') and (self.password == '123'):
            print('----- successfully logged -------')

            self.options() # calling method internally

        else:
            print('Invalid credentials. Please try again....')

    def options(self):

        self.ops = ('Choose below options to perform such operation \
                    \n1 Balance, 2 Deposit, 3 Withdraw, 4 Exit ')

        print(self.ops)

        self.ops_input = input("Choose Options : ")
        print(self.ops_input)

        if self.ops_input == '1':
            print('Balance Operation')
            self.balance()

        elif self.ops_input == '2':
            print("Deposit Operation")
            self.deposit()

        elif self.ops_input == '3':
            print("Withdraw Operation")

        elif self.ops_input == '4' :
            print("Exit Operation")
            exit()

        else:
            print('Invalid option')

    def balance(self):
        # self.bal = 0
        print(f'Balance : {Bank.bal} ') # calling SV

        self.options()

    def deposit(self):
        self.damount = int(input('Enter Deposit Amount : '))
        Bank.bal = Bank.bal + self.damount

        print(self.bal)

        self.options()

    def withdrawl(self):
        self.wamount = int(input('Enter wamount Amount : '))
        Bank.bal = Bank.bal - self.wamount

        print(self.bal)

        self.options()


c1 = Bank()





