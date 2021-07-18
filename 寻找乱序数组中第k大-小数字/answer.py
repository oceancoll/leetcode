# coding:utf-8
"""
寻找乱序数组中，第k大/小的数字
思路：
    根据快排的思想，以及二分法策略进行查找
    输入：[1,3,5,4,2,6,8], 3
    查找第3大的数字，输出5
"""
def findKNum(arr, k):
    count = len(arr)
    # 第K大
    # return quick(arr, 0, count-1, count-k)
    # 第K小
    return quick(arr, 0, count-1, k-1)
def quick(arr, left, right, K):
    slow, fast = left, right
    key = arr[left]
    while left<right:
        while left<right and arr[right]>=key:
            right-=1
        arr[left] = arr[right]
        while left<right and arr[left]<=key:
            left+=1
        arr[right] = arr[left]
    arr[right] = key
    if right==K:
        return arr[right]
    elif right>K:
        return quick(arr, slow, right-1, K)
    else:
        return quick(arr, right+1, fast, K)
print findKNum([1,3,5,4,2,6,8], 1)