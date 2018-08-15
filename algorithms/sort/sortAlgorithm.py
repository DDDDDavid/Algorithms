#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 14 18:13:13 2018

@author: madawei1
"""
x=[3,2,1,4,9,34,5]
n=len(x)

#冒泡排序
def BubblingSort(x,n):
    for i in range(0,n):
        for j in range(i,n):
            tmp=x[i]
            if x[i]<x[j]:
                x[i]=x[j]
                x[j]=tmp
    return x

#插入排序
def InsertionSort(x,n):
    
    return x

#简单选择排序
def SelectionSort(x,n):
    
    return x

#希尔排序
def ShellSort(x,n):
    
    return x

#归并排序
def MergeSort(x,n):
    
    return x

#快速排序
def QuickSort(x,n):
    
    return x

#堆排序
def HeapSort(x,n):
    
    return x

#计数排序
def CountingSort(x,n):
    
    return x


#桶排序
def BucketSort(x,n):
    
    return x

#基数排序
def RadixSort(x,n):
    
    return x

                


x0=x.copy()
y0=BubblingSort(x0,n)   
print(y0)