# coding:utf-8
"""八大排序算法"""
a = [2,5,1,3,8,5,7,4,3]

"""
冒泡法
左右两个数据进行对比，大的数据位于右侧，小的数据位于左侧
每一次排序会选出剩余数的最大值
时间复杂度为：n^2,稳定
"""
def maopao(origin):
    count = len(origin)
    for i in range(count):
        for j in range(count-i-1):
            if origin[j] > origin[j+1]:
                origin[j], origin[j+1] = origin[j+1], origin[j]
    return origin


"""
选择法
每一轮排序选出剩余所有数的最小值，排到对应的位次
使用交换法，将对应的数交换到对应位次
时间复杂度为：n^2，不稳定
"""
def xuanze(origin):
    count = len(origin)
    for i in range(count):
        smallindex= i
        for j in range(i,count):
            if origin[smallindex] > origin[j]:
                smallindex = j
        origin[smallindex], origin[i] = origin[i], origin[smallindex]
    return origin


"""
插入法
从第一位开始，每一位数，插入到已经排序列表的对应位置，对已排序列表的查询从后到前搜索
时间复杂度：n^2， 稳定
"""
def charu(origin):
    count = len(origin)
    for i in range(1, count):
        key = origin[i]
        j = i
        while j>=1 and origin[j-1]>key:
            origin[j] = origin[j-1]
            j-=1
        origin[j] = key
    return origin

"""
希尔排序
根据步长将列表分为多个组，以步长不断向后搜索，直到结尾。依次类推，可以分为多个组，组内的排序使用插入法进行排序。不断的缩小步长。进而排序
时间复杂度：nlogn，不稳定
"""
def shell(origin):
    count = len(origin)
    gap = count/2
    while gap>0:
        for i in range(gap, count):
            key = origin[i]
            j = i
            while j>=gap and origin[j-gap]>key:
                origin[j] = origin[j-gap]
                j-=gap
            origin[j] = key
        gap/=2
    return origin

"""
快排法
选取第一个值作为基准值，先从右向左查询，当遇到小于基准值时，停止。再从左向右查询，遇到大于基准值时，停止。将左右俩个值交换。
再从右向左，从左向右。直到两个指针碰面。
此时将左右分为2部分，再分别对左边和右边进行递归，进而排序
时间复杂度：nlogn，不稳定
"""
def quick(origin, left, right):
    if left >= right:
        return origin
    key = origin[left]
    low = left
    high = right
    while left < right:
        while left < right and origin[right] >= key:
            right-=1
        origin[left] = origin[right]
        while left < right and origin[left] <= key:
            left += 1
        origin[right] = origin[left]
    origin[right] = key
    quick(origin, low, right-1)
    quick(origin, right+1, high)
    return origin

"""
归并排序
从左到右，相邻的两个数为一组，进行对比排序。再以相邻的两组进行合并排序，依次递归
时间复杂度：nlogn，基数排序
"""
def merge(left, right):
    result = []
    while left and right:
        if left[0]<right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    if right:
        result += right
    return result

def merge_sort(origin):
    count = len(origin)
    if count <2:
        return origin
    mid = count/2
    left = origin[:mid]
    right = origin[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

"""
基数排序
从列表中的数的个位开始，进行分桶，一共有10个桶。排完后，再根据十位数进行分桶，依次递归，直到最高位
时间复杂度：logRB(B是真数(0-9),R是基数(个十百))，稳定
"""
def jishu_sort(origin):
    maxnum = max(origin)
    maxlen = len(str(maxnum))
    for i in range(maxlen):
        tmp = [[]for _ in range(10)]
        for j in origin:
            tmp[int(j/10**i)%10].append(j)
        origin = []
        for x in tmp:
            for y in x:
                origin.append(y)
    return origin

"""
堆排序(大顶堆) 小顶堆同理
大顶堆，二叉树结构，每个根大于两个子节点
https://blog.csdn.net/lerry13579/article/details/82052429
     0
   1   2
 3  4 5 6
7 8
"""
def HeapSort(origin):
    def heapadjust(origin, parent, length):
        temp = origin[parent]
        # 根的左节点
        child = 2*parent+1
        while child < length:
            # 左右节点进行比较
            if child+1< length and origin[child+1]>origin[child]:
                child+=1
            # 根最大退出
            if origin[child]<temp:
                break
            # 深度搜索
            origin[parent] = origin[child]
            parent = child
            child= 2*child+1
        origin[parent] = temp

    if not origin:
        return []
    count = len(origin)
    # 先根据列表生成一个大顶堆
    # 从最后一个满行堆最左侧的值开始
    for i in range(0, count/2)[::-1]:
        heapadjust(origin, i, count)
    for j in range(1, count)[::-1]:
        # 顶和最后一个值进行交换，选出最大值
        origin[0], origin[j] = origin[j], origin[0]
        # 剩余的元素再进行堆整合
        heapadjust(origin, 0, j)
    return origin

print jishu_sort(a)