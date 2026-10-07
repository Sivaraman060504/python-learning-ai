import matplotlib.pyplot as plt

marks= [90,91,92,80,83,86,78,71]

plt.hist(marks)
plt.xlabel("marks")
plt.ylabel("no of students")
plt.title("marks distribution")

plt.show()