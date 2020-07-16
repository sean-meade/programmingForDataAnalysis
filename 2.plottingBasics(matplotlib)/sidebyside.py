import matplotlib.pyplot as plt
import numpy as np

#This subplot will have 1 row, 2 plots and this will be the first in it
plt.subplot(1, 2, 1)
x = np.random.normal(0.0, 1.0, 10000)
plt.hist(x)

plt.subplot(1, 2, 2)
x = np.random.uniform(-3.0, 3.0, 10000)
plt.hist(x)

plt.show()