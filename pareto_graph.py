import numpy as np
import matplotlib.pyplot as plt
a, m = 6., 2.  # 分布の幅と、モードを指定
s = (np.random.pareto(a, 1000) + 1) * m
#  ヒストグラムを描画
count, bins, _ = plt.hist(s, 100, density=True)

# 線グラフの描画
fit = a * m ** a / bins ** (a + 1)
plt.plot(bins, max(count) * fit / max(fit), linewidth=2, color='r')
plt.show()
