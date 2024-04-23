class student:
    def grade(self):
        s1 = int(input("Enter s1 marks : "))
        s2 = int(input("Enter s2 marks : "))
        s3 = int(input("Enter s3 marks : "))

        print(s1,s2,s3)

        total = s1 + s2 + s3
        print(f'total : {total}')
        avg = total // 3
        print(f'avg : {avg}')

        if avg > 90:
            print('grade : O')

        elif (avg > 80) and (avg < 90):
            print('grade : A')

        elif (avg > 60) and (avg < 80):
            print('grade : B')

        else:
            print('grade : Failed')


std1 = student()

std1.grade()



# create a 'Bank'  class with 'deposit' method
# sv : bname,baddress,cname,cadd,caccount, cbal = 0
#
# in method---
# nsv : damount ---> realtime i/p
# Bank.cbal = Bank.cbal+damount
# print(Bank.cbal)