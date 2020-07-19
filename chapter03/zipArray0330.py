#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-19 18:37:17
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np
a=np.arange(5)
print(a)
# clip 设置阈值
print(a.clip(1,2))
# compress 根据条件进行筛选
print(a.compress(a>2))

