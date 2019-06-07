import numpy as np
import matplotlib.pyplot as plt

print("平均を入力せよ")
avg = int(input())
print("分散を入力せよ")
variance = int(input())

std_deviation = np.sqrt(variance)

print("平均: %d, 分散: %d" % (avg, variance))

# 平均 avg, 標準偏差 std_deviation の正規乱数を1件生成
x = np.random.normal(avg, std_deviation, 1)
print(x)
