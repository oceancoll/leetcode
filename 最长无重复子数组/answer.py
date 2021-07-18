# coding:utf-8
"""
给定一个数组，找出最长的无重复子数组的长度是多少
输入：[1,2,3,1,2,3,2,2] 输出：3
输入：[2,2,3,4,8,99,3] 输出：5

思路：
    用一个临时数组，存当前满足周期内的数。
    注意：当遇到相同值时，从相同值的地方进行截断，相当于是又一轮的开始
    比如[7，8，9，1,2,3,1,2,3],遇到第二个1时，从第一个1的位置进行截断，从而可以继续累加第2次的1
"""
def maxLength(arr):
    maxl = 0
    tmps = []
    for i in arr:
        if i in tmps:
            maxl = max(maxl, len(tmps))
            index = tmps.index(i)
            tmps = tmps[index+1:]
        tmps.append(i)
    return max(maxl, len(tmps))  # 判断最后一轮的长度与历史长度的大小