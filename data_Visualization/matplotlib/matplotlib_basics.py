import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [10,25,15,50,30]

plt.plot(x,y)
plt.title("my first graph")
plt.show()


day = [1,2,3,4,5]
working = [10,8,9,7,6]


#plt.scatter(day,working)
#plt.plot(day,working)
#plt.bar(day,working)


plt.plot(day,working)
plt.title("graph for my working time")
plt.xlabel("week days")
plt.ylabel("no of hours working per day")
plt.show()