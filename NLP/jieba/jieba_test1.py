# -*- coding: utf-8 -*-
"""
Created on Mon Apr  2 17:37:41 2018

@author: madawei1
"""

# encoding=utf-8
import jieba
import jieba.posseg as pseg

seg_list = jieba.cut("我来到北京清华大学", cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

seg_list = list(jieba.cut("我来到北京清华大学", cut_all=False))
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

seg_list = jieba.cut("他来到了网易杭研大厦")  # 默认是精确模式
print(", ".join(seg_list))

seg_list = jieba.cut_for_search("小明硕士毕业于中国科学院计算所，后在日本京都大学深造")  # 搜索引擎模式
print(", ".join(seg_list))

words = pseg.cut("我爱北京天安门")
for word, flag in words:
    print('%s %s' % (word, flag))
    
jieba.load_userdict('keyword/keywords2.0.txt') 

print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))
jieba.suggest_freq(('中', '将'), True) #调整词频
print('/'.join(jieba.cut('如果放到post中将出错。', HMM=False)))

print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))
jieba.suggest_freq('台中', True)
print('/'.join(jieba.cut('「台中」正确应该不会被切开', HMM=False)))

#返回词语在原文的起止位置
result = jieba.tokenize(u'永和服装饰品有限公司')
for tk in result:
    print("word %s\t\t start: %d \t\t end:%d" % (tk[0],tk[1],tk[2]))
    
