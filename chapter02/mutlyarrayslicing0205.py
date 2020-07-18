#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-07-18 11:23:59
# @Author  : helingjie-maskmind (helingjie440@gmail.com)
# @Link    : ${link}
# @Version : $Id$

import os
import numpy as np

b=np.arange(24).reshape(2,3,4)

print(b.shape)
print(b)

print(b[0,0,0])
print(b[:,0,0])

print(b[0,:,:])
print(b[0,...])

print(b[0,1])
print(b[0,1,::2])

print(b[...,1])
print(b[:,1])

print(b[0,:,1])
print(b[0,:,-1])
print(b[0,::-1,-1])
print(b[0,::2,-1])

print(b[::-1])