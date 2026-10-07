import matplotlib.pyplot as plt

days =[1,2,3,4,5]
sales = [20,30,40,30,20]
expenses =[10,15,12,13,15]

fig,ax=plt.subplots(2,1)

ax[0].bar(days,sales)
ax[0].set_title("Sales")

ax[1].bar(days,expenses)
ax[1].set_title("expenses")

plt.tight_layout()

#savefig is used to save the graph 
plt.savefig("Sales.png")
plt.show()
