# Backward index ----> right to left ----> -1

x = 'Hello' # -5-,4,-3,-2,-1

# note : print fn prints always left to right

# using backward undex print 'o'

print(x[-1])

print(x[-4])

# slicing

# 'Hel'

print(x[-5:-2]) # upper bound is always should be greater than lower bound (u-1) -3-1 = -4

print(x[-5:-3]) # -3-1 = -4 ---> e

# -5  to -2-1 --> -3 ---> l

#

a = 'Good Morning'

# print Morning
print(a[-7:-1]) # -1-1 == -2
print(a[-7:])

# Good
print(a[-12:-8])

# both formawd and backward

print(a[0:-1]) # if we are using both lower bound shoud should be forward

print(x[-1:0]) # 0-1 = -1 # invalid format









