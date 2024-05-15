
from deposit import Deposit
from withdrawl import Withdraw
from balance import Balance



class Bank:
    try:
        bank_name = 'HDFC'
        bank_address = 'Sathupalli'

        print('Bank Name',bank_name)
        print('Bank Address',bank_address)

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
            try:

                self.ops = ('Choose below options to perform such operation \
                            \n1 Balance, 2 Deposit, 3 Withdraw, 4 Exit ')

                print(self.ops)

                self.ops_input = input("Choose Options : ")
                print(self.ops_input)

                if self.ops_input == '1':
                    print('Balance Operation')
                    Balance().balance(Bank.bal)
                    self.options()

                elif self.ops_input == '2':
                    print("Deposit Operation")
                    Bank.bal = Deposit().deposit(Bank.bal)
                    print(Bank.bal)
                    self.options()
                elif self.ops_input == '3':
                    print("Withdraw Operation")
                    Bank.bal = Withdraw().withdraw(Bank.bal)
                    print(Bank.bal)
                    self.options()

                elif self.ops_input == '4' :
                    print("Exit Operation")
                    exit()

                else:
                    print('Invalid option')

            except Exception as e:
                print('Error occured in option method',e)

    except Exception as e:
        print('Error occured in Class defining',e)



