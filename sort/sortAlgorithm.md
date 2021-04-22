## 排序算法总结

### 排序算法

#### 一、冒泡排序
冒泡排序算法的运作如下：

1.比较相邻的元素。如果第一个比第二个大，就交换他们两个。
2.对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
3.针对所有的元素重复以上的步骤，除了最后一个。
4.持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

代码实现：
```python
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
```

#### 二、选择排序
选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。

代码实现：
```python
# 简单选择排序
def selection_sort(arr):
    n =len(arr)
    for i in range(0,n):
        for j in range(i,n):
            if arr[i]>arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
    return arr
```

#### 三、插入排序

步骤如下

1.从第一个元素开始，该元素可以认为已经被排序
2.取出下一个元素，在已经排序的元素序列中从后向前扫描
3.如果该元素（已排序）大于新元素，将该元素移到下一位置
4.重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
5.将新元素插入到该位置后
6.重复步骤2~5


代码实现
```python
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
```
#### 四、希尔排序

希尔排序通过将比较的全部元素分为几个区域来提升插入排序的性能。这样可以让一个元素可以一次性地朝最终位置前进一大步。然后算法再取越来越小的步长进行排序，算法的最后一步就是普通的插入排序，但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）。

代码实现：
```python
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
```
#### 五、归并排序

原理如下（假设序列共有{displaystyle n}个元素）：
1.将序列每相邻两个数字进行归并操作，形成{displaystyle ceil(n/2)}个序列，排序后每个序列包含两/一个元素
2.若此时序列数不是1个则将上述序列再次归并，形成{displaystyle ceil(n/4)}个序列，每个序列包含四/三个元素
3.重复步骤2，直到所有元素排序完毕，即序列数为1

代码如下：
```python
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
```
#### 六、快速排序

1.从数列中挑出一个元素，称为“基准”（pivot），
2.重新排序数列，所有比基准值小的元素摆放在基准前面，所有比基准值大的元素摆在基准后面（相同的数可以到任何一边）。在这个分割结束之后，该基准就处于数列的中间位置。这个称为分割（partition）操作。
3.递归地（recursively）把小于基准值元素的子数列和大于基准值元素的子数列排序。
4.递归到最底部时，数列的大小是零或一，也就是已经排序好了。这个算法一定会结束，因为在每次的迭代（iteration）中，它至少会把一个元素摆到它最后的位置去。

代码如下：

```python
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

```
#### 七、堆排序

若以升序排序说明，把数组转换成最大堆积(Max-Heap Heap)，这是一种满足最大堆积性质(Max-Heap Property)的二叉树：对于除了根之外的每个节点i, A[parent(i)] ≥ A[i]。

重复从最大堆积取出数值最大的结点(把根结点和最后一个结点交换，把交换后的最后一个结点移出堆)，并让残余的堆积维持最大堆积性质。

```python
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
```


#### 八、计数排序
```python
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
```

#### 九、基数排序
```python

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
```

#### 十、桶排序
代码略


#### 附：数据测试代码
```python
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
```
