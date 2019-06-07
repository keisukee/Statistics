import numpy as np
import matplotlib.pyplot as plt

sample_amount = 10000

# データの観測範囲を指定。0から100まで。つまり、偏差値0から偏差値100まで計測可能
data_range_min = 0
data_range_max = 100
data_range_spread = data_range_max - data_range_min
avg = 50 # 平均
variance = 10 # 分散
spread = 1 # x軸の間隔を決める。spreadは必ずdata_range_spreadを割り切れる値にすること
std_deviation = np.sqrt(variance) # 標準偏差

# 平均 avg, 標準偏差 std_deviation の正規乱数をsample_amount件生成
data_set = np.random.normal(avg, std_deviation, sample_amount)
data_set.sort()
each_data_in_spread = [] # 各範囲に存在するdata_setの数値を入れる

for i in range(0, int(data_range_spread/spread)): # 100はデータの分割個数
    each_data_in_spread.append([]) # 二次元配列
    for j in range(0, sample_amount):
        if (i * spread) <= data_set[j] <= ((i + 1) * spread): # 例えば、50.0以上50.2以下ならdata_set[j]は区間49~50, つまりeach_data_in_spreadの500番目に入る
            each_data_in_spread[i].append(data_set[j])
        elif data_set[j] > ((i + 1) * spread): # data_setはsortしてあるので、あるデータが測定範囲を超えたら後はスキップして良い
            break

# 各区間の出現回数を数える
num_of_occur = []
for i in range(0, int(data_range_spread/spread)):
    num_of_occur.append(len(each_data_in_spread[i]))

# x軸は最小値data_range_min, 最大値data_range_max, 間隔spread
x = np.arange(data_range_min, data_range_max, spread)
y = num_of_occur
plt.plot(x, y) # 正規分布を描く（標準正規分布ではないことに注意）
plt.show()

# 各範囲のデータが出現する確率を入れる。例えば、ある生成されたデータが49以上50以下の範囲にある確率は、occur_probability[50]に入る
occur_probability = []

for i in range(0, int(data_range_spread/spread)):
    p = num_of_occur[i] / sample_amount # 各区間の値が出現する確率を算出。発生回数 / 総試行回数
    occur_probability.append(p)

y_op = occur_probability
plt.figure()
plt.plot(x, y_op) # 標準正規分布を描く
# SND: standart normal distribution
plt.savefig("SND_avg=%d_var=%d.png" % (avg, variance))
plt.show()

# 確率分布を求める
sum_of_probability = []
for i in range(0, int(data_range_spread/spread)): # 区間0からiまでの確率の総和を求める
    probability_range = 0
    for j in range(0, i):
        probability_range += occur_probability[j]
    sum_of_probability.append(probability_range)

y_sop = sum_of_probability
plt.figure()
plt.plot(x, y_sop) # 確率分布を描く
# PDF: probability density function
plt.savefig("PDF_avg=%d_var=%d.png" % (avg, variance))
plt.show()
