# coding:utf-8
"""
给定无序数组arr，返回其中最长的连续序列的长度(要求值连续，位置可以不连续,例如 3,4,5,6为连续的自然数）
输入：[100,4,200,1,3,2]
输出：4 // [1,2,3,4]

输入：[1,1,1]
输出：1 // [1]

思路：先使用set将数组变为集合，然后依次遍历集合，判断n-1数字是否在set中，如果不在，说明是新的一个连续开始
此时，更新最大连续个数为1，然后不断去检查n+1是否在set中，从而获得最长个数
"""
def longestConsecutive(nums):
    nums =set(nums)
    maxlength = 0
    for i in nums:
        if i-1 not in nums:
            currLenght = 1
            while i+1 in nums:
                currLenght +=1
                i+=1
            maxlength = max(maxlength, currLenght)
    return maxlength
print longestConsecutive([1,1,1])