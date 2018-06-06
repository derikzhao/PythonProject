# -*- coding: utf-8 -*-

import numpy as np

# Ndarray对象
a = np.array([1, 2, 3])
a1 = np.arange(10)

print(a)
print(a1)

# 数据类型
print('-------------------------------')
b = np.arange(5)
print(b.dtype)
print (np.dtype("f4"))
print(np.int32)
print(np.dtype(np.int32))

studentDt = np.dtype([('name', 'S20'), ('age', 'i1'), ('marks', 'f4')])  # 端标记
aStu = np.array([('abc', 21, 50), ('xyz', 18, 75)], dtype=studentDt)
print(studentDt)
print(aStu)
print(aStu["age"])

# 使用zeros/empty
print('-------------------------------')

print(np.zeros(10))
print(np.zeros((2, 3)))
print(np.empty([2, 2], dtype=int))
print(np.ones([2, 2]))

# 属性
print('-------------------------------')

a4 = np.array([[1, 2, 3], [4, 5, 6]])
print a4.shape  # 数组维度

a4.shape = (3, 2)
print(a4)
print(a4.reshape(1, 6))  # 调整数组大小

print(np.arange(24).reshape(2, 4, 3))

print(np.arange(10).itemsize)
print(np.arange(5).flags)

# 数值范围数组
# numpy.arange(start, stop, step, dtype)
print('-------------------------------')

print(np.arange(0, 10, 3, dtype=int))
print(np.linspace(0, 20, 5, True))
