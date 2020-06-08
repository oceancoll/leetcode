# coding:utf-8
"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
你可以假设数组中无重复元素。
    示例 1:
        输入: [1,3,5,6], 5
        输出: 2
    示例 2:
        输入: [1,3,5,6], 2
        输出: 1
    示例 3:
        输入: [1,3,5,6], 7
        输出: 4
    示例 4:
        输入: [1,3,5,6], 0
        输出: 0
链接：https://leetcode-cn.com/problems/search-insert-position
https://leetcode-cn.com/problems/search-insert-position/solution/er-fen-fa-by-li-jun-yu-3/
"""
def searchInsert(nums, target):
    count = len(nums)
    left = 0
    right = count-1
    ans = -1
    while left<=right:
        mid = (left+right)/2
        if nums[mid]>=target:
            right = mid-1
            ans = mid
        else:
            left = mid+1
    return ans

