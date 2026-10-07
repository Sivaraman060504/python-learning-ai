import matplotlib.pyplot as plt

days=[1,2,3,4,5]
sales=[25,30,21,43,54]

#size of the graph ex : width and heigth
plt.figure(figsize=(12,5))

plt.plot(sales,days,label="overall sales")
plt.title("sales")
plt.xlabel("sales")
plt.ylabel("days")

plt.legend()

plt.show()
