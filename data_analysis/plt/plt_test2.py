# -*- coding: utf-8 -*-
"""
Created on Thu Apr 12 16:00:19 2018

@author: madawei1
"""

import numpy as np  
import matplotlib.pyplot as plt  
  
x = np.arange(0, 100)  
  
plt.subplot(221)  
plt.plot(x, x)  
  
plt.subplot(222)  
plt.plot(x, -x)  
  
plt.subplot(223)  
plt.plot(x, x ** 2)  
  
plt.subplot(224)  
plt.plot(x, np.log(x))  
  
plt.show()  


#面向对象
import numpy as np  
import matplotlib.pyplot as plt  
  
x = np.arange(0, 100)  
  
fig = plt.figure()  
  
ax1 = fig.add_subplot(221)  
ax1.plot(x, x)  
  
ax2 = fig.add_subplot(222)  
ax2.plot(x, -x)  
  
ax3 = fig.add_subplot(223)  
ax3.plot(x, x ** 2)  
  
ax4 = fig.add_subplot(224)  
ax4.plot(x, np.log(x))  
  
plt.show()  