# -*- coding: utf-8 -*-

import numpy as np

print '读取csv文件做为数组'
arr = np.loadtxt('../array_ex1.txt', delimiter = ',')
print arr