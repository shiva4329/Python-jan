

class Withdraw:
    def withdraw(self,bal):
        self.wamount = int(input('Enter wamount Amount : '))
        if self.wamount > bal:
            print('Insufficient funds')
        else:
            bal = bal - self.wamount
        return bal