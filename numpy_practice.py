import numpy as np

np.random.seed(42)
marks=np.random.randint(0,101,(5,3))

print("marks:",marks)

print("\nshape:",marks.shape)
print("\nmax:",marks.max())
print("\nmin:",marks.min())
print("\navarege:",marks.mean())