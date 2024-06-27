import matplotlib.pyplot as plt

x = [0,1,2,3,4,5] # defining x axis values
y = [10,20,10,30,50,60] # defining y axis values

plt.plot(x,y,'--', color = 'yellow',marker = 'o') # plotting the line graph
# graph formats
# : = doted
# - = solid line
# -- = dashed line
# -. = dash doted line




plt.title('Sample',color = 'red') # title of graph
plt.xlabel('Time',color = 'pink') # assigning x axis name
plt.ylabel('Speed',color = 'green') # asssigining y axis name

plt.legend()
plt.show() # displaying the graph