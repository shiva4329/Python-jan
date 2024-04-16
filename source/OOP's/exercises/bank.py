


class bank:

    name = 'HDFC'
    add = 'HYD'

    bal = 0

    def deposit(self):
        bank.bal = int(input("Enter deposit amount : ")) + bank.bal

    def balance(self):

        print(bank.bal)




c1 = bank()

c1.deposit()

c1.balance()