import numpy as np #毎度おなじみ
import matplotlib.pyplot as plt #毎度おなじみ
from scipy.stats import norm



x = np.arange(1500, 3000) # 1500～3000の要素が入ったリストを作る
y = norm.cdf(x, loc=2000, scale=60) # 平均2000，標準偏差60の正規分布の累積分布関数

plt.figure(0)
plt.grid(True)
plt.plot(x, y)
plt.xlabel("value")
plt.ylabel("probability")
plt.savefig("ruiseki.png", dpi=200)
plt.show()
