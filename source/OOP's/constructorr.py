# constructer : when we are calling 'class' it automatically executes
#               defining using '__init__'
#               it is also called as method no need to call seperately, it executes directly when we are calling class




class calculator:

    def __init__(self): # constructor
        self.bank = 'hdfc'
        self.x = 10
        self.y = 20
        print(self.x + self.y)
        print('im constructor')

    def display(self): # method
        print('Im display')




obj = calculator()



# create a 'student' class, create a 'grade' method

# take i/p  for 3 subjs
# find avg
# grade assign

# each subj total = 100
#
# 10,20,30 = avg


# if avg > 90:
#     "o"
#
#     avg <90 >80
#     "A"
#
#     avg >60 <80
#     "B"


