#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 15:08:47
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

N = int(input("输入weight大小"))

weights = np.ones(N) / N
print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
print(c)
# convolve卷积 开始到结束区间
sma = np.convolve(weights, c)[N-1:-N+1]
print(sma)

t = np.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
show()
