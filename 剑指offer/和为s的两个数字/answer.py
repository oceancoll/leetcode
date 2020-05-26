# coding:utf-8
"""
和为s的两个数字

输入一个递增排序的数组和一个数字s，在数组中查找两个数，
使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可

输入：nums = [2,7,11,15], target = 9
输出：[2,7] 或者 [7,2]

"""

def twoSum(nums, target):
    """
    双指针法
    一个从前到后，一个从后到前。
    大于时右指针减1，小于时左指针加1，等于时输出
    :param nums:
    :param target:
    :return:
    """
    count = len(nums)
    i = 0
    j = count-1
    while i<j:
        if nums[i]+nums[j]==target:
            return [nums[i],nums[j]]
        elif nums[i]+nums[j]>target:
            j-=1
        else:
            i+=1
    return []
