#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:13:13 2018

@author: madawei1

https://www.cnblogs.com/huang-yc/p/9774287.html
"""


#冒泡排序
def bubble_sort(arr):
    n =len(arr)
    for i in range(n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    res = arr
    return res

#插入排序
def InsertionSort(arr):
    
    return res

#简单选择排序
def SelectionSort(arr):
    
    return res

#希尔排序
def ShellSort(arr):
    
    return res

#归并排序
def MergeSort(arr):
    
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
res =    
print(res)
