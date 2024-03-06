# find a maximum number using while loop without max()

x = [10,30,60,20,40,50]

c = 0
m = x[0]

while c < len(x): # 0 < 5, 1 < 5
    # print(x[c])

    if x[c] > m:
        m = x[c]

    c = c + 1
print(m)

# w.a.p to sort a list using while loop with out sorted()
x = [30,20,10,40]

# create a real-time list using while loop

# ip = int(input('Enter range of value : '))
# lis = []
# c = 0

# while c < ip:

#     lis.append(c)
#     # print(lis)
#     c = c + 1

# print(lis)


# create a real-time list with even numbers using while loop

ip = int(input('Enter range of value : '))
lis = []
c = 0

while c < ip:
    if c%2 == 0:
        lis.append(c)
    # print(lis)
    c = c + 1

print(lis)