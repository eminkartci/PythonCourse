import numpy as np
import matplotlib.pyplot as plt

# 3x11 -- 1
oneMatrix = np.ones([3,11])
print(oneMatrix.shape)
print(oneMatrix.sum())
print(oneMatrix.max())

hours = np.arange(24*7)
rainfals = np.random.rand(24*7,1) * 40
rainfals2 = np.random.rand(24*7,1) * 40
rainfals3 = np.random.rand(24*7,1) * 40
print(hours)
print(rainfals)

np.savetxt("rainfalls.csv", rainfals, delimiter=",")
plt.plot(hours,rainfals,"r")
plt.plot(hours,rainfals2,"g--")
plt.plot(hours,rainfals3,"bo")
plt.show()


        

