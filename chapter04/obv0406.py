#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 23:48:50
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

c, v=np.loadtxt('BHP.csv', delimiter=',', usecols=(6, 7), unpack=True)
# 前后差值
change = np.diff(c)
print(change)
# 判断符号
signs = np.sign(change)
print("Signs", signs)
# 判断符号
pieces = np.piecewise(change, [change < 0, change > 0], [-1, 1])
print("Pieces", pieces)
# 判断得到的数组是否相等
print(np.array_equal(signs, pieces))

print(v[1:] * signs)

