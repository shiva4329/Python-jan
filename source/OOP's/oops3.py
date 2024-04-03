# write a progam to find even or odd, i/p real time


# using functions

# num = int(input('Enter a number : '))
def even(num):
    if num % 2 == 0:
        print(num,'is an even number')
    else:
        print(num, 'is odd number')

# even(num)



# using oops


num = int(input('Enter a number : ')) # global
class number:

    def even(self,num):
        if num % 2 == 0:
            print(num, 'is an even number')
        else:
            print(num, 'is odd number')



number().even(num)
