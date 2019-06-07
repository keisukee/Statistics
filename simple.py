from math import *
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

x = sym.symbols('x')
pi = np.pi
e = np.e

x = np.arange(-10, 10, 0.1)
y = (1/(np.sqrt(2*pi))) * e**(-x**2/2)
# p = sym.integrate(y, (x, -1, 1))
y = (1.0 + erf(x / sqrt(2.0))) / 2.0
plt.plot(x,y)
plt.show()
