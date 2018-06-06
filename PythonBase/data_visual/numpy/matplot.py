# encoding:UTF-8
import sys

reload(sys)
sys.setdefaultencoding('gbk')

import numpy as np
from numpy.linalg import cholesky
import matplotlib.pyplot as plt
import pylab

# 直方图
sampleNo = 1000;
mu = 85
sigma = 4
np.random.seed(0)
s = np.random.normal(mu, sigma, sampleNo)
plt.hist(s, 30, normed=True)
pylab.show()

# 线性图
x = np.arange(1, 11)
y = 2 * x + 5
plt.title("Matplotlib demo")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y, 'vb')
plt.show()

x = np.arange(0, 3 * np.pi, 0.1)
print(x)
y = np.sin(x)
plt.title("sine wave form")
# 使用 matplotlib 来绘制点
plt.plot(x, y)
plt.show()

# 计算正弦和余弦曲线上的点的 x 和 y 坐标
x = np.arange(0, 3 * np.pi, 0.1)
y_sin = np.sin(x)
y_cos = np.cos(x)
# 建立 subplot 网格，高为 2，宽为 1
# 激活第一个 subplot
plt.subplot(2, 1, 1)
# 绘制第一个图像
plt.plot(x, y_sin)
plt.title('Sine')
# 将第二个 subplot 激活，并绘制第二个图像
plt.subplot(2, 1, 2)
plt.plot(x, y_cos)
plt.title('Cosine')
# 展示图像
plt.show()
