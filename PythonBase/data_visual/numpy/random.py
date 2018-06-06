# encoding:UTF-8

import numpy.random as np_random
import numpy as np

# 随机浮点数
print(np_random.random())
print(np_random.random((3, 2)))

# 随机整数
print(np_random.randint(2))
print(np_random.randint(2, size=(2, 4)))

# 高斯分布随机数
print(np_random.normal(loc=0.0, scale=1, size=(2, 3)))

# 标准正态分布
print(np_random.randn(4, 2))

# [0,1)随机数
print(np_random.rand(2, 3))

# 随机打乱序列

x = [1, 2, 3, 4, 5]
print(x)
print(np_random.shuffle(x))

# 随机选取
print(np_random.choice(5, 6))
print(np_random.choice(5, 3, p=[0.1, 0, 0.3, 0.6, 0]))

# 二项分布采样

print sum(np_random.binomial(5, 0.2, size=10000) == 0) / 10000.

# 指定种子值
print(np_random.RandomState(0).randint(8))


