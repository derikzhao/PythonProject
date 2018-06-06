# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from pandas import Series

# 数组生成Series
print('--------------数组生成Series-----------------')
s = pd.Series(np.arange(5))
print(s)

# 指定索引
print('--------------指定索引-----------------')
s2 = pd.Series(np.arange(5), index=list('aasdf'))
print(s2)
print(s2['a'])

# 使用字典创建
print('--------------使用字典创建-----------------')

data = {'a': 0., 'b': 1., 'c': 2.}
s3 = pd.Series(data)
print(s3)
print(pd.Series(data, index=list("abcd")))  # 缺失用NaN填充

# 访问数据
print('--------------访问数据-----------------')
print(s3[:2])
print(s3['a'])
