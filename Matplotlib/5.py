import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]

x2 = [1,2,3]
y2 = [10,14,12]

x3 = [1,2,3]
y3 = [5,10,15]

# here we are using plot 2 times so we will get the line graph two times
plt.plot(x, y, label='First Line',color = 'black')
plt.plot(x2, y2, label='Second Line')
plt.plot(x3, y3, label='Third Line')

plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()