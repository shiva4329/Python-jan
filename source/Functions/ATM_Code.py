from colorama import Fore
# step1 : login
# step2 : Ask options
# step3 : if succesfully logged in ask for option(withdrawl,deposit,balance,exit)

user = 'ABC'
pwd = '123456'
balance = 1000

def bal(): # balance fn
    global balance
    print(f"\t\tbalance : {balance}\n")

def deposit(): # deposit fn
    global balance
    amount = int(input('Enter deposit Amount : '))
    balance = balance + amount
    # print(f"\t\tbalance : {balance}\n")

def withdrawl(): # withdrawl fn
    global balance
    amount = int(input('Enter withdrawl Amount : '))
    if amount > balance :
        print('Insufficient funds')
    else:
        balance = balance - amount
    # print(f"\t\tbalance : {balance}\n")



def options(): # options fn
    msg = '''1  Balance     2   Deposit \n3  Withdrawl    4   Exit\n'''
    print(msg)

    opt = int(input('Choose above options : '))

    if opt == 1:
        bal()
        options()
    elif opt == 2:
        deposit()
        options()
    elif opt == 3:
        withdrawl()
        options()
    elif opt == 4:
        exit()
    else:
        print('--Invalid option--')
        options()


def login(user,pwd): # login fn

    if user == 'ABC' and pwd == '123456':
        print('Successfully Logged')
        options() # calling options fn here
    else:
        print('Invalid Credentials, please try after some time')

login(user,pwd)