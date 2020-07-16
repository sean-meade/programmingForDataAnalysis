import matplotlib.pyplot as plt#
import numpy as np

x = np.random.uniform(0.0, 10.0, 100)
y = np.random.uniform(0.0, 100.0, 100)
# size of dot
z = np.random.normal(100.0, 40.0, 100)
# colour of dot
c = np.random.randint(0, 20, 100)

# 4d plot
plt.scatter(x, y, c=c, s=z)

plt.show()

x = np.arange(-2.0 * np.pi, 2.0 * np.pi, 0.1)

plt.plot(x, np.sin(x), 'g.')
plt.plot(x, np.cos(x), 'b.')

plt.show()

x = np.arange(1.0, 100.0, 0.1)

plt.plot(x, x**2, 'g-', label="x^2")
plt.plot(x, x**3, 'b-', label="x^3")
plt.plot(x, x**4, 'r-', label="x^4")
plt.plot(x, 2**x, 'k-', label="2^x")

plt.legend()
plt.show()