import numpy as np
import matplotlib.pyplot as plt
from numpy.random import *
import sys
from decimal import *
from random import expovariate

l = list(range(1))

for i in range(20000):
    l.append(expovariate(2))

plt.hist(l, bins=100)
filename="expovariate_hist1.png"
plt.savefig(filename)
plt.show()
