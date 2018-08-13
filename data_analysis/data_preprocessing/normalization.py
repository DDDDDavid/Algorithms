#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 15:49:23 2018

@author: madawei1
"""

import math
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 100, 101)
xmax = max(x)
xmin = min(x)
xmean = np.mean(x)
xvar = np.var(x)

def nor(x,xmax):
    y=x/xmax
    return y

#min-max标准化
def min_max(x,xmax,xmin):
    y=(x-xmin)/(xmax-xmin)
    return y

def min_max_mean(x,xmax,xmin,xmean):
    y=(x-xmean)/(xmax-xmin)
    return y

#z-score
def z_mean(x,xmean,xvar):
    y=(x-xmean)/xvar
    return y

def nor_log10(x,xmax):
    y = [math.log10(i)/math.log10(xmax) for i in x]
    return y

def nor_atan(x):
    y=[math.atan(i)*2/math.pi for i in x]
    return y

#小数定标标准化
def dec_scale(x):
    xabs=max(abs(x))
    xscale =math.ceil(math.log10(xabs))
    y= x/math.pow(10,xscale)
    return y

def sigmoid(x,a=1,b=0):
    y=[1/(1+math.exp(-(a*i+b))) for i in x]
    return y

#模糊量化
def fuzzy_quant(x,xmax,xmin):
    y=[0.5+0.5*math.sin(math.pi/(xmax-xmin)*(i-(xmax-xmin)/2)) for i in x]
    return y
    
 
y0 = nor(x,xmax)
plt.subplot(121)
plt.title("nor_log10")
plt.plot(x,y0)   

y1 = min_max(x,xmax,xmin)
plt.subplot(122)
plt.title("min-max")
plt.plot(x,y1)
plt.show()

y2 = min_max_mean(x,xmax,xmin,xmean)
plt.subplot(121)
plt.title("min-max-mean")
plt.plot(x,y2)


y3 = z_mean(x,xmean,xvar)
plt.subplot(122)
plt.title("z_mean")
plt.plot(x,y3)
plt.show()

y4 = nor_log10(x,xmax)
plt.subplot(121)
plt.title("nor_log10")
plt.plot(x,y4)

y5 = nor_atan(x)
plt.subplot(122)
plt.title("nor_atan")
plt.plot(x,y5)
plt.show()

y6 = dec_scale(x)
plt.subplot(121)
plt.title("dec_scale")
plt.plot(x,y6)

y7 = sigmoid(x)
plt.subplot(122)
plt.title("sigmoid")
plt.plot(x,y7)
plt.show()

y8 = fuzzy_quant(x,xmax,xmin)
plt.subplot(121)
plt.title("fuzzy_quant")
plt.plot(x,y8)

plt.show()