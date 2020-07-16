# This is for 1D data
import matplotlib.pyplot as plt
import numpy as np

# Shows a normal standard deviation distribution
x = np.random.normal(0.0, 1.0, 1000)

# Finds the lowest value of x, then finds the biggest value of x,
# then it chops that range up into a number of bins (10 as default).
# Then a histogram shows how many values of x are in each bin.
plt.hist(x, bins=20)

plt.show()