# in python we have 4 types of varibales
#   types :
#             global
#             local
#             static
#             non-static

# global variable : declaring the variable outside the fn/class
#                     global varaible can access anywhere in the code

# ex:

# in function

# x = 10 # global
# def sample()
#     pass

# in class

# x = 10 # global
#
# class sample:
#     def sample(self):
#         pass



# local varable : declating the variables with-in the fn
#                  can be accessed only with-in the fn


# ex:

# in function

# x = 10 # global
# def sample()
#     y = 10 # local
#     pass



# static varable: declaring with-in the class, not with-in the method
#                   static variables can access anywhere with-in the class
#               but by using classname we can access outside the class
#                   syntax of ouside the class : ex: classname.staticvarname


# in class

# x = 10 # global
#
# class sample:

#     y = 20 # static

#     def sample(self):
#         pass



# non-static varable: declaring with-in the method, not with-in the class
#                   non-static varabless can declared using 'self'
#                   non-static variables can access with in the method/class


# in class

# x = 10 # global
#
# class sample:

#     y = 20 # static

#     def sample(self):
#       z = 30 # local
#       self.z = 30 # non-static
#         pass