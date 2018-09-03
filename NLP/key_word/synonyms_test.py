#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 14:17:27 2018

@author: madawei1
"""

import synonyms

#中文分词
synonyms.seg("中文近义词工具包")

#nearby
print("破洞: " ,(synonyms.nearby("破洞")))
print("女人: " ,(synonyms.nearby("女人")))
print("NOT_EXIST: " ,(synonyms.nearby("NOT_EXIST")))

sen1 = "快递"
sen2 = "物流"
r = synonyms.compare(sen1, sen2, seg=True)