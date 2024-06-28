import matplotlib.pyplot as plt

x = [0,1,2,3,4,5] # defining x axis values
y = [10,20,10,30,50,60] # defining y axis values

plt.plot(x,y,marker='o',color = 'red') # plotting the line graph
# shapes in marker
#  o = circle
#  * = star
# . = point
# + = plus
# D,d = diamond
# H,h = hexagon
# ^,>,<,v = triangle


plt.title('Sample') # title of graph
plt.xlabel('Time') # assigning x axis name
plt.ylabel('Speed') # asssigining y axis name

plt.show() # displaying the graph