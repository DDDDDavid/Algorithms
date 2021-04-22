#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:13:13 2018

@author: madawei1

https://www.cnblogs.com/huang-yc/p/9774287.html
"""


# 冒泡排序
## 相邻的数据两两比较，较小的排前面
def bubble_sort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(1,n-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
    return arr
##优化，增加一个flag，无需继续排序则停止
def bubble_flag_sort(arr):
    n =len(arr)
    flag = True
    for i in range(n):
        for j in range(1,n-i):
            if arr[j-1]>arr[j]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                flag = False #没有发生交换
        if flag:
            return arr
    return arr


# 简单选择排序
## 
def selection_sort(arr):
    n =len(arr)
    for i in range(0,n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
    

#插入排序
def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        if arr[i] < arr[i-1]:
            temp = arr[i]
            index = i
            for j in range(i-1,-1,-1):
                if arr[j] > temp:
                    arr[j+1] = arr[j]#向后移位
                    index = j
                else:
                    break
            arr[j] = temp
    return arr


#希尔排序
def shell_sort(arr):
    n = len(arr)
    gap = n//2
    while gap > 0:
        for i in range(gap,n):
            temp = arr[i]
            j = i
            while j > gap and arr[j-gap] > temp:
                arr[j] = arr[j-gap]
                arr[j-gap] = temp
            gap = gap//2
    return arr

#归并排序
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr)//2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left,right)

def merge(left,right):
    l,r = 0,0
    res = []
    while l < len(left) and r <len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    res += right[r:]
    res += left[l:]
    return res
            

#快速排序
def quick_sort(arr):
    less = []
    pivotlist = []
    more = []
    if len(arr) <= 1:
        return arr 
    else:
        #第一个值为基准
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                #比基准小的放到less
                less.append(i)
            elif i > pivot:
                #比基准大的放到more
                more.append(i)
            else:
                #等于基准的放到pivotlist
                pivotlist.append(i)
        #less和more继续排序
        less = quick_sort(less)
        more = quick_sort(more)
    return less + pivotlist + more
##快速排序精简写法
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(greater)
## 一行语法糖写法    
qs = lambda xs : ( (len(xs) <= 1 and [xs]) or [ qs( [x for x in xs[1:] if x < xs[0]] ) + [xs[0]] + qs( [x for x in xs[1:] if x >= xs[0]] ) ] )[0]

#堆排序
def heap_sort(list):
    # 创建最大堆
    for start in range((len(list) - 2) // 2, -1, -1):
        sift_down(list, start, len(list) - 1)

    # 堆排序
    for end in range(len(list) - 1, 0, -1):
        list[0], list[end] = list[end], list[0]
        sift_down(list, 0, end - 1)
    return list

# 最大堆调整
def sift_down(lst, start, end):
    root = start
    while True:
        child = 2 * root + 1
        if child > end:
            break
        if child + 1 <= end and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] < lst[child]:
            lst[root], lst[child] = lst[child], lst[root]
            root = child
        else:
            break
    return res

#计数排序
def count_sort(arr):
    min = 2147483647
    max = 0
    # 取得最大值和最小值
    for x in arr:
        if x < min:
            min = x
        if x > max:
            max = x
    # 创建数组C
    count = [0] * (max - min +1)
    for index in arr:
        count[index - min] += 1
    # 填值
    index = 0
    for a in range(max - min + 1):
        for c in range(count[a]):
            arr[index] = a + min
            index += 1
    return arr    




#基数排序
def radix_sort(arr):
    n = len(str(max(arr)))
    i = 0
    while i < n:
        bucket_list = [[] for _ in range(10)]
        for x in arr:
            bucket_list[int(x/(10**i))%10].append(x)
        #打印基数排序过程
        #print(bucket_list)
        arr.clear()
        for x in bucket_list:
            for y in x:
                arr.append(y)
        i += 1
    return arr

#桶排序
def bucket_sort(arr):
    return res

arr=[3,2,1,9,4,9,34,5,45656,6874,54,44]  
print('arr',arr)
          
res = bubble_sort(arr)
print('bubble_sort:',res)

res = selection_sort(arr)
print('selection_sort',res)

res = insert_sort(arr)
print('insert_sort',res)

res = shell_sort(arr)
print('shell_sort',res)

res = merge_sort(arr)
print('merge_sort',res)

res = quick_sort(arr)
print('quick_sort',res)

res = qsort(arr)
print('qsort',res)

res = qs(arr)
print('qs:', res)

res = heap_sort(arr)
print('heap_sort:', res)

res = count_sort(arr)
print('count_sort:', res)

res = radix_sort(arr)
print('radix_sort:', res)