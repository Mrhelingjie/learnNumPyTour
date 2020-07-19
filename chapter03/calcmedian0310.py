#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 00:02:46
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

c=np.loadtxt('data.csv',delimiter=',',usecols=(6,),unpack=True)
# 计算中位数
print("median",np.median(c))
# 传统方法计算中位数
sorted=np.msort(c)
n=len(c)
print("middle=",sorted[int((n-1)/2)])
print("average middle=",(sorted[int(n/2)]+sorted[int((n-1)/2)])/2)

# 计算方差
print("variance",np.var(c))
print("define variance=",np.mean((c-c.mean())**2))