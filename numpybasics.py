import numpy as np 
numbers = np.array([10,20,30,40,50])
print(numbers)


a=[1,2,3]
b=np.array([
    [1,2,3],
           [2,4,5]])

print(a*2)
print(b*2)

print(a+a)
print(b+b)

print(b.shape)



onee = np.ones(5)
print(onee)

zero = np.zeros(5)
print(zero)

arrange = np.arange(1,10)
print(arrange)

arangewith = np.arange(4,24,4)
print(arangewith)