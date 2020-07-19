#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 23:54:19
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

high,low=np.loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack=True)
print("lowest",np.min(low))
print("highest",np.max(high))
print(np.max(high)-np.min(low))

print(np.ptp(high))
print(np.ptp(low))