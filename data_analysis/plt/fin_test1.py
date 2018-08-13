# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:58:14 2018

@author: madawei1
"""
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import randn

fig =plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
plt.plot(randn(50).cumsum(), 'r')
ax1.hist(randn(100),bins =20,color ='k',alpha=0.3)
ax2.scatter(np.arange(30),np.arange(30)+3*randn(30))