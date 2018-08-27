### list转str
#### 1、" ".join(list)
    
join函数，推荐使用，引号内空格可以替换
```
list1=['a','b','c']  
str1=" ".join(list1)

> str1='a b c'
```

#### 2、str(list)

直接转str，会存储引号和方括号

```
list1=['a','b','c']  
str1=str(list1)

> str1="['a', 'b', 'c']"
```

### str转list
#### str.split()

split函数，引号内符号可以替换
```
str1='a b c'  
list1=str1.split(" ")

>list1=['a','b','c']
```

### str转int  
#### int()
int_value = int(str_value)  
### int转str
#### str()
str_value = str(int_value)

### bool转str
#### str()  
str_value = str(bool_value)
### str转bool
#### 1、bool()
在python中，除了''、""、0、()、[]、{}、None为False， 其他转换都为True  
#### 2、使用判断，只有str_value为true时候，转为true的布尔类型
data = "True"  
isTrue = data == str_value




