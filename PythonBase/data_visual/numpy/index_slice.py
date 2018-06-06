# -*- coding: utf-8 -*-

import numpy as np

# 一维数组
print('-------------------------------')
a = np.arange(10)
s = slice(2, 7, 2)
print(a[s])
print(a[2:])
print(a[2:5])

# 多维数组
print('-------------------------------')
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr)
print arr[0]  # 结果是个2维数组
print arr[1, 0]  # 结果是个1维数组

# 切片 （数据视图）
print('-------------------------------')

a2 = np.array([[1, 2, 3], [3, 4, 5], [4, 5, 6]])
print(a2[1:3])
print(a2[0, ...])  # 第一行
print(a2[..., 0])  # 第一列
print(a2[0:2, 0:2])  # 1-2行，1-2列

# 高级索引--整数,（返回数据副本，导致复制）
print('-------------------------------')
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

print(x[[0, 1, 2], [0, 1, 0]])

rows = np.array([[0, 0], [3, 3]])
cols = np.array([[0, 2], [0, 2]])
y = x[rows, cols]
print  '这个数组的每个角处的元素是：'
print y

# 高级索引--布尔,（返回数据副本，导致复制）
print('-------------------------------')
x2 = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])

print(x2[x > 5])