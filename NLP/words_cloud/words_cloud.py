#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 10:05:17 2018

@author: madawei1
"""

import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS, ImageColorGenerator
import jieba
 
text_from_file_with_apath = open('./resource/data/guichuideng.txt',encoding='utf-8').read()
 
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

# 设置停用词
stopwords = set(STOPWORDS)
stopwords.add("我们")
 
color_mask = plt.imread("./resource/data/danghui.jpg")
cloud = WordCloud(
    #设置字体，不指定就会出现乱码
    font_path="./fonts/msyh.ttf",
    #设置停用词
    stopwords=stopwords,
    #设置背景色
    background_color='white',
    #词云形状
    mask=color_mask,
    #允许最大词汇
    max_words=2000,
    #最大号字体
    max_font_size=400
)

my_wordcloud = cloud.generate(wl_space_split)
my_wordcloud.to_file("./resource/data/guichuideng.jpg") #保存图片
 
plt.imshow(my_wordcloud,interpolation="bilinear") 
plt.axis("off")
plt.show()
plt.imsave('./resource/data/guichuideng.png',my_wordcloud)# 保存图片