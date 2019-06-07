import numpy as np
from numpy.random import *
import matplotlib.pyplot as plt
from scipy.stats import norm
import math

pi = np.pi
e = np.e
# データの観測範囲を指定。0から100まで。つまり、偏差値0から偏差値100まで計測可能
data_range_min = 0
data_range_max = 100
data_range_spread = data_range_max - data_range_min
spread = 1 # x軸の間隔を決める。spreadは必ずdata_range_spreadを割り切れる値にすること
sample_amount = 10000

print("平均を入力せよ")
avg = int(input())
print("分散を入力せよ")
variance = int(input())
std_deviation = np.sqrt(variance)
print("平均: %d, 分散: %d" % (avg, variance))

box_muller_data = rand(int(sample_amount/2), 2) # 1セットから2つの確率変数が得られるのでsample_amountを2で割っている
data_set = []
for i in range(0, int(sample_amount/2)):
    data_set.append(np.sqrt(-2*math.log(box_muller_data[i][0])) * math.cos(2*pi*box_muller_data[i][1]))
    data_set.append(np.sqrt(-2*math.log(box_muller_data[i][0])) * math.sin(2*pi*box_muller_data[i][1]))

data_set.sort()

std_normal_data = []
for i in range(0, sample_amount):
    x = np.sqrt(variance) * data_set[i] + avg
    y = (1/(np.sqrt(2*pi*variance))) * e**(-(x-avg)**2/(2*variance))
    std_normal_data.append(y)
    print(y)

# plt.hist(std_normal_data, bins=100)
#
# plt.savefig("box_muller_hist_var=%d_avg=%d.png" % (variance, avg))
# plt.show()
