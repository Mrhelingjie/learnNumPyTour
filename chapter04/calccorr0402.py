#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 23:28:24
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# 加载信息
bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
bhp_returns = np.diff(bhp) / bhp[ : -1]
vale = np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[ : -1]

# 计算协方差矩阵
convariance=np.cov(bhp_returns,vale_returns)
print(convariance)
# 矩阵的对角线元素
print(convariance.diagonal())
# 矩阵的迹
print(convariance.trace())
# 定义计算矩阵相关系数
print(convariance/(bhp_returns.std()*vale_returns.std()))
# numpy直接计算矩阵相关系数
print(np.corrcoef(bhp_returns,vale_returns))

difference =bhp - vale
# 均值
avg=np.mean(difference)
# 标准差
dev=np.std(difference)
# 偏差是否符合
print(np.abs(difference[-1]-avg)>2*dev)

t=np.arange(len(bhp_returns))
plot(t,bhp_returns,lw=1)
plot(t,vale_returns,lw=2)
show()