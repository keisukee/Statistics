import matplotlib.pyplot as plt
import numpy as np
import sympy as sym
sym.init_printing()
oo = sym.oo # 無限大
(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z) = sym.symbols('a b c d e f g h i j k l m n o p q r s t u v w x y z')


# -300 < x < 300, 0.1間隔
z = np.arange(-1000, 1000, 0.1)
# x = np.arange(-10, 10, 0.1)

pi = np.pi
e = np.e
# 分散
s = 100
# 標準偏差
m = np.sqrt(s)
# 平均
avg = 50

y_1 = (1/(np.sqrt(2*pi*s))) * e**(-(z-avg)**2/(2*s))
x = (z-avg)/s
y = (1/(np.sqrt(2*pi))) * e**(-x**2/2)

# グラフへのプロット実行
# plt.plot(z, y_1)
plt.plot(x, y)
plt.show()

# 確率p
# y = x**2
# p = sym.integrate(a, (b, -10, 10))
p = sym.integrate(y, (x, -1, 1))
# print(p)
