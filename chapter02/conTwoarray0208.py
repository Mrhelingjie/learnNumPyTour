#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 13:17:32
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

a=np.arange(9).reshape(3,3)
print(a)

b=2*a
print(b)

# 横向组合
print(np.hstack((a,b)))
print(np.concatenate((a,b),axis=1))
# 垂直组合
print(np.vstack((a,b)))
print(np.concatenate((a,b),axis=0))
# 深度组合
print(np.dstack((a,b)))

# 列组合
print(np.column_stack((a,b)))
# 二维数组情况下雨hstack效果相同
# 可用==判断两个numpy数组是否相同
print(np.column_stack((a,b))==np.hstack((a,b)))

# 行组合
print(np.row_stack((a,b)))
# 二维数组情况下与vstack效果相同
print(np.row_stack((a,b))==np.vstack((a,b)))
