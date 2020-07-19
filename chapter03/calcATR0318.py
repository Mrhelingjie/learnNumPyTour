#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 14:50:08
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
from datetime import datetime

h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

N = int(input("输入N"))
# 取得最近的几个交易日数据
h = h[-N:]
l = l[-N:]
print("len(h)", len(h), "len(l)", len(l))
print("Close", c)
# 为前一天的收盘价格 向前平移一个单位
previousclose = c[-N -1: -1]
print("Previous close", previousclose)

# 三个数组中元素最大值
truerange = np.maximum(h - l, h - previousclose, previousclose - l) 
# 方便查看
print (truerange.reshape(4,4))

atr = np.zeros(N)
atr[0] = np.mean(truerange)

# 计算接下来的atr
for i in range(1,N):
    atr[i]=(N-1)*atr[i-1]+truerange[i]
    atr[i]/=N

print(atr)