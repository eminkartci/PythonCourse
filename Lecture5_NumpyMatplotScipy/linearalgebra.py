import numpy as np


A = np.array([
    [1 ,4 ,6],
    [4 , 63 ,1], 
    [325, 53, 2]
])

b = np.array([36, 54, 2])

x = np.linalg.solve(A,b)

print(x)