# -*- coding: utf-8 -*-

import numpy as np

# 数组上的迭代
print('-------------------------------')

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print(a)

for x in np.nditer(a, order="F"):
    pass
    # print(x)

# 数组操作--reshape 不改变数据的条件下修改形状
# numpy.reshape(arr, newshape, order')
print('-------------------------------')

print(np.arange(20).reshape(4, 5))

# 数组操作--flat 数组上的一维迭代器
print('-------------------------------')
print(np.arange(20).reshape(4, 5).flat[5])

# 数组操作--flatten 返回折叠为一维的数组副本
# ndarray.flatten(order)
print('-------------------------------')
print(np.arange(20).reshape(4, 5).flatten())

# 数组操作--ravel 返回连续的展开数组
# numpy.ravel(a, order)
print('-------------------------------')

# 数组操作--翻转,转置
# numpy.transpose == numpy.T
# numpy.transpose(arr, axes)
print('-------------------------------')
print(np.arange(20).reshape(4, 5).transpose())
print(np.arange(20).reshape(4, 5).T)

# 数组连接--
# numpy..concatenate((a1, a2, ...), axis)
print('--------------数组连接-----------------')
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(np.concatenate((a, b)))

print(np.stack((a, b), 0))  # 沿新轴连接
print(np.hstack((a, b)))
print(np.vstack((a, b)))

# 数组分割--
# numpy.split(ary, indices_or_sections, axis)
print('--------------数组分割-----------------')

print(np.split(np.arange(9), 3))
print(np.split(np.arange(9), [4, 7]))
print(np.hsplit(np.arange(16).reshape(4, 4), 2))
print(np.vsplit(np.arange(16).reshape(4, 4), 2))

# 添加/删除元素--
#
print('--------------添加/删除元素-----------------')
arr_a = np.arange(6).reshape(2, 3)

print(np.resize(arr_a, (3, 2)))

print(np.append(arr_a, [7, 8, 9]))
print(np.append(arr_a, [[7, 8, 9]], axis=0))
print(np.insert(arr_a, 2, [[7, 8, 9]], axis=0))
print(np.insert(arr_a, 6, [7, 8, 9]))  # 沿着它插入的轴，如果未提供，则输入数组会被展开
print(np.delete(arr_a, 1, axis=1))

arr_b = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])
print(np.unique(arr_b))
