#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 23:39:35
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
# 读取数据
bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
vale = np.loadtxt('VALE.csv', delimiter=',', usecols=(6,), unpack=True)

t=np.arange(len(bhp))
# 多项式拟合
poly=np.polyfit(t,bhp-vale,int(input("please input N")))

print(poly)
# 通过计算得出的多项式对象 推断下一个值
print(np.polyval(poly,t[-1]+1))
# 求多项式的根
print(np.roots(poly))
# 求导
der = np.polyder(poly)
print(der)
# 求导函数的根 => 极值点
print (np.roots(der))
# 计算多项式的值
vals = np.polyval(poly, t)
print (np.argmax(vals))
print (np.argmin(vals))

plot(t, bhp - vale)
plot(t, vals)
show()