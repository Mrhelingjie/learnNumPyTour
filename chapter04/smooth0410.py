#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-20 00:00:30
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(input("N"))
# hanning平滑函数
weights = np.hanning(N)
print ("Weights", weights)
# 读取并得出数据
bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
bhp_returns = np.diff(bhp) / bhp[ : -1]
# 与weight卷积得到收益率
smooth_bhp = np.convolve(weights/weights.sum(), bhp_returns)[N-1:-N+1]

vale = np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[ : -1]
smooth_vale = np.convolve(weights/weights.sum(), vale_returns)[N-1:-N+1]


K = int(input("input"))
t = np.arange(N - 1, len(bhp_returns))
# 多项式拟合
poly_bhp = np.polyfit(t, smooth_bhp, K)
poly_vale = np.polyfit(t, smooth_vale, K)
# 对两个多项式做差
poly_sub = np.polysub(poly_bhp, poly_vale)
# 求根
xpoints = np.roots(poly_sub)
print ("Intersection points", xpoints)
# 是否为实数
reals = np.isreal(xpoints)
print(reals)
# 取得实数
xpoints = np.select([reals], [xpoints])
xpoints = xpoints.real
print(xpoints)
# 去掉前后的0
print(np.trim_zeros(xpoints))

# 画图
plot(t, bhp_returns[N-1:], lw=1.0)
plot(t, smooth_bhp, lw=2.0)
plot(t, vale_returns[N-1:], lw=1.0)
plot(t, smooth_vale, lw=2.0)
show()
