# pdf: probability density function, 確率密度関数
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from math import *

x = np.arange(-100, 200, 0.1) # 1500～3000の要素が入ったリストを作る
data_sets = [[50, 10],[50, 50],[50, 100], [50, 500], [50, 1000]]
for data in data_sets:
    plt.figure()
    y = norm.pdf(x, loc=data[0], scale=sqrt(data[1])) # 平均40，標準偏差10の正規分布の累積分布関数
    plt.plot(x, y)
    plt.savefig("pdf_avg=%d_var=%d.png" % (data[0], data[1]))
