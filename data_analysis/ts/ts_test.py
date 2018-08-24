#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:38:00 2018

@author: madawei1
"""

import tushare as ts

data=ts.get_today_all()
news=ts.guba_sina()