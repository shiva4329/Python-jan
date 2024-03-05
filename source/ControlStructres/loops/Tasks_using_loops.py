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

x = [10,30,20,50,40] # Ascending order = [10,20,30,40,50]