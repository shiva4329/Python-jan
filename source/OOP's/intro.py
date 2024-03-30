# oop's : object oriented programming structure
# oops is based objects
# oops is like blue-print of the code


# example :

# in banking sector
#       customers are objects
#       blue print is the banaking structre(like cr,db,bal checking)



# advantages
#         security
#         re-usability
#         flexibility


# types: 4 pillers of oops
#       Encapsulation : binds the data + operations
#       In-heritence : including one obj properties into another obj
#       Abstract : providing security to objcts
#       Polymorphism : many forms




# syntax :

# class <name>:
#     def <method_name>(self):
#         pass



# sample program

class sample:
    print('Im sample class')
    def display(self): # method
        print('Im display method')

sample().display()



# creating home structure

class home:
    print('Im in home')
    def kitchen(self):
        print('im kitchen')
    def bedroom(self):
        print('Im bed room')
    def work_room(self):
        print('Im working room')



# home().work_room()

# customer 1
obj1 = home()
obj1.work_room()

# customer 2
obj2 = home()
obj2.kitchen()

# customer 3
obj3 = home()
obj3.bedroom()

# customer 4
obj4 = home()
obj4.bedroom()
obj4.kitchen()
obj4.work_room()

