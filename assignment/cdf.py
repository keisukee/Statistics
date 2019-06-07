# cdf: cumulative distribution function, 累積分布関数
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import *

x = np.arange(0, 100, 0.1) # 1500～3000の要素が入ったリストを作る
data_sets = [[50, 10],[50, 50],[50, 100], [50, 500], [50, 1000]]
for data in data_sets:
    plt.figure()
    y = norm.cdf(x, loc=data[0], scale=sqrt(data[1])) # 平均40，標準偏差10の正規分布の累積分布関数
    plt.plot(x, y)
    plt.savefig("cdf_avg=%d_var=%d.png" % (data[0], data[1]))
