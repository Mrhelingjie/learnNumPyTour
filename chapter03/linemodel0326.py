#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 17:58:28
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
import sys

N = int(input("please input N"))
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)

# 包含N个股价的向量b
b = c[-N:]
print(b)
b = b[::-1]
print("b", b)

A = np.zeros((N, N), float)
for i in range(N):
   A[i, ] = c[-N -1- i:-1 - i]

print("A", A)
(x, residuals, rank, s) = np.linalg.lstsq(A, b)

print(x, residuals, rank, s)
print(x.shape)
# 点积 b=> 1xN x=>Nx1
print(np.dot(b, x))

