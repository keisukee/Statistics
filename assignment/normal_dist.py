import numpy as np
import matplotlib.pyplot as plt

print("平均を入力せよ")
avg = int(input())
print("分散を入力せよ")
variance = int(input())

std_deviation = np.sqrt(variance)

print("平均: %d, 分散: %d" % (avg, variance))

# 平均 avg, 標準偏差 std_deviation の正規乱数を10000件生成
x = np.random.normal(avg, std_deviation, 10000)
data_sample100 = np.random.normal(avg, std_deviation, 100)
data_sample500 = np.random.normal(avg, std_deviation, 500)
data_sample1000 = np.random.normal(avg, std_deviation, 1000)
data_sample5000 = np.random.normal(avg, std_deviation, 5000)
data_sample10000 = np.random.normal(avg, std_deviation, 10000)

# ヒストグラムを出力
plt.hist(x, bins=100)
filename="hist_var=1000.png"
plt.savefig(filename)
# plt.show()

# plt.hist(data_sample100, bins=50)
# filename="hist100.png"
# plt.savefig(filename)
#
# plt.hist(data_sample500, bins=50)
# filename="hist500.png"
# plt.savefig(filename)
#
# plt.hist(data_sample1000, bins=50)
# filename="hist1000.png"
# plt.savefig(filename)
#
# plt.hist(data_sample5000, bins=100)
# filename="hist5000.png"
# plt.savefig(filename)
#
# plt.hist(data_sample10000, bins=100)
# filename="hist10000.png"
# plt.savefig(filename)
