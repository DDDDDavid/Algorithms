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
        if l == len(left):
            res += right[r:]
        elif r ==len(right):
            res += left[l:]
    return res
            

#快速排序
def QuickSort(arr):
    
    return res

#堆排序
def HeapSort(arr):
    
    return res

#计数排序
def CountingSort(arr):
    
    return res


#桶排序
def BucketSort(arr):
    
    return res

#基数排序
def RadixSort(arr):
    
    return res

arr=[3,2,1,4,9,34,5]  
          
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