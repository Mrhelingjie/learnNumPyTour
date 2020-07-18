#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 18:56:27
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

b=np.arange(81).reshape(9,9)
com=np.array([1+1.j,3+2.j])
print(com.tolist())
print(b.tolist())

print(com.astype(int))