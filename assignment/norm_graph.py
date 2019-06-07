import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
# -300 < x < 300, 0.1間隔
x = np.arange(0, 100, 1)

pi = np.pi
e = np.e
# 分散
variance = 100
# 平均
avg = 50

y_1 = (1/(np.sqrt(2*pi*variance))) * e**(-(x-avg)**2/(2*variance))
z = (x-avg)/np.sqrt(variance)
y = (1/(np.sqrt(2*pi))) * e**(-z**2/2)

# グラフへのプロット実行
# plt.plot(z, y_1)
plt.plot(x, y)
plt.show()
