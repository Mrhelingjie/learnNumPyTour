#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 23:32:26
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

c,v=np.loadtxt('data.csv',delimiter=',',usecols=(6,7),unpack=True)

vwap=np.average(c,weights=v)
print('vwap=',vwap)

# 算术平均数
print(np.mean(c))

t=np.arange(len(c))
twap=np.average(c,weights=t)
print(twap)