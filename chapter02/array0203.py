#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 10:54:15
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

t=np.dtype([('name',np.str_,40),('numitems',np.int32),('price',np.float32)])
print(t)
print(t['name'])


itemz = np.array([('Meaning of life DVD', 42, 3.14), ('Butter', 13, 2.72)], dtype=t)
print(itemz[0])