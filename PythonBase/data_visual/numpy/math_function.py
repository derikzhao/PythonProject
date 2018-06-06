# -*- coding: utf-8 -*-

import numpy as np

# 算数函数--
#
print('--------------三角函数-----------------')
a = np.array([0, 30, 45, 60, 90])
a_pi = a * np.pi / 180
print(np.sin(a_pi))
print(np.cos(a_pi))
print(np.tan(a_pi))

print('--------------舍入函数-----------------')
a_around = np.array([1.0, 5.55, 123, 0.567, 25.532])
print(np.around(a_around, decimals=1))
print(np.around(a_around, decimals=-1))

print(np.floor(a_around))
print(np.ceil(a_around))

print(np.sqrt(a_around))
print(np.square(a_around))

print('--------------算数运算-----------------')
# add()，subtract()，multiply()和divide()
a_add = np.arange(9, dtype=np.float_).reshape(3, 3)

print(np.add(a_add, [10, 10, 10]))
print(np.subtract(a_add, [10, 10, 10]))
print(np.multiply(a_add, [10, 10, 10]))
print(np.divide(a_add, [10, 10, 10]))

print(np.reciprocal(a_add))


