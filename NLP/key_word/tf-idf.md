# tf-idf

tf-idf是一种统计方法，可以计算提取文本集合中特征词。

tf：term frequency，分词出现频率

`tf=(某个分词数量)/(文本总词数量)`

idf：inversedocument frequency，逆向文件频率

`idf=log((全部文本数量/出现某个分词文本数量)+1)`

tf-idf:

`tf-idf=tf*idf`

# jieba分词中的tf-idf

[结巴分词关键词提取]http://www.cnblogs.com/zhbzz2007/p/6177832.html

`tf_idf=jieba.analyse.extract_tags(sentence, topK=500, withWeight=False, allowPOS=())`

结巴分词中的tf值取的是文本中词的频率除以文本中词的总频率。  
***但是！！！***  
结巴分词中的idf值默认取idf词典及idf中值（如果某个词没有出现在idf词典中，则将idf中值作为这个词的idf值）。
