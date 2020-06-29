import matplotlib.pyplot as plt
import numpy as np

# Give me all the values between zero (including zero) and ten (not including ten) in 
# increments of zero point zero one (0.01).
x = np.arange(0.0, 10.0, 0.01)
y = 3.0 * x + 1.0

# Create noise with center zero, a standard deviation (or scale) of one, and size is the same 
# as the size of x.
noise = np.random.normal(0.0, 1.0, len(x))

plt.plot(x, y + noise, 'r.')
plt.plot(x, y, 'b-')
plt.show()


plt.plot(x, y + noise, 'c.')
plt.plot(x, y, 'g-')
plt.show()