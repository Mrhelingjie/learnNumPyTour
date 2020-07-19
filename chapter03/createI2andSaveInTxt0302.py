#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 23:10:26
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$


# numpy创建一个单位矩阵并写入到txt
import os
import numpy as np

# 建单位矩阵
i2=np.eye(2)
print(i2)
# 写入到txt
np.savetxt("eye.txt",i2)