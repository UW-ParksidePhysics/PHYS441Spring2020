import numpy as np
import matplotlib.pyplot as plt

pi = np.pi
a = 2* pi* 1.0

x_values = np.linspace(0, a, 1000) #evaluating psi at these x values

A = (2/a)**1/2 #normalization constant

def psi(n, x):
    wave_function = A* np.sin(n* pi* x/a) #define our function
    return wave_function

y_values1 = psi(1, x_values)
y_values2 = psi(2, x_values)
y_values3 = psi(3, x_values)

plt.plot(x_values, y_values1, 'k', linewidth = 2.0, label = 'n=1')
plt.plot(x_values, y_values2, 'r', linewidth = 0.7, label = 'n=2')
plt.plot(x_values, y_values3, 'b', linewidth = 0.7, label = 'n=3')
plt.legend()
plt.title('Wave function for Infinite Square Well')
plt.xlabel('x values')
plt.ylabel('$\psi$(x)')
plt.grid
plt.show()
