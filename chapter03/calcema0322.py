#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 15:18:52
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

x=np.arange(5)
print("exp",np.exp(x))
print("linspace",np.linspace(-1,0,5))


N=int(input("please input N"))
weights = np.exp(np.linspace(-1.,0.,N))
weights/=weights.sum()

print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights, c)[N-1:-N+1]

t = np.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, ema, lw=2.0)
show()
