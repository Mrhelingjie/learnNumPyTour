#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 12:37:07
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

b=np.arange(24).reshape(2,3,4)
# ravel 只是返回数组的一个视图
print(b.ravel())

# flatten 展平数组，会请求分配内存来保存结果
print(b.flatten())

b.shape=(6,4)

print(b)

# 矩阵的转置
# b.transpose()不直接修改b
print(b.transpose())
# reshape不直接修改b
# b.reshape(3,8)
# print(b)
b.resize(2,12)
print(b)