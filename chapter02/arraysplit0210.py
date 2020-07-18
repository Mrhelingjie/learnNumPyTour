#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 17:37:45
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np


a=np.arange(9).reshape(3,3)
# 水平分割
print(np.hsplit(a,3))
print(np.split(a,3,axis=1))
# 垂直分割
print(np.vsplit(a,3))
print(np.split(a,3,axis=0))
# 深度分割
c=np.arange(27).reshape(3,3,3)
print(c)
print(np.dsplit(c,3))
