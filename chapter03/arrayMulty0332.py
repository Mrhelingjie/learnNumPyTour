#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 18:40:28
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
a=np.arange(1,9)
print(a)
# prod 计算数组元素乘积
print(a.prod())
# cumprod 计算数组元素累积乘积
print(a.cumprod())