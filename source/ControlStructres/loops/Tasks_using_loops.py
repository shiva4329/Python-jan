# w.a.p to find maximum number in list using for loop with out max()

# x = [10,20,30]

# print(max(x))

x = [10,2000,300,40]
m = x[0] # initalize the 1st value in list for using comparision

for i in range(len(x)):
    if m < x[i]:
        m = x[i]
        
print(m)


# w.a.p to find minimum number in list using for loop with out max()

x = [10,2000,300,40]
m = x[0] # initalize the 1st value in list for using comparision

for i in range(len(x)):
    if m > x[i]:
        m = x[i]
        
print(m)


# w.a.p to sort ascending order of list using for loop with out sort()

x = [10,30,20,50,40,10] # Ascending order = [10,20,30,40,50]

for i in range(0,len(x)):
    for j in range(i+1,len(x)):
        if x[i] > x[j]:
            x[i],x[j] = x[j],x[i] # 10,30 = 30,10

print(x)



# create a list with 20 values using range()

x = []

for i in range(1,20+1):
    x.append(i)
print(x)

y = list(range(1,20+1))
print(y)


# create a list with even numbers upto 20, using range(20)

x = []

for i in range(1,20+1):
    if i%2 == 0:
        x.append(i)
print(x)

# create a list by giving user input as a range(user_input)

ip = int(input("Enter range value : "))

lis = []

for i in range(1,ip+1):
    lis.append(i)

print(lis)