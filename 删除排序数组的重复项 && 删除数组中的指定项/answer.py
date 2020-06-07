# coding:utf-8
"""
删除排序数组的重复项
https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
也就是说不能开辟新空间，将非重复元素在前面一次排列，重复的可以排在后面，最后返回非重复的个数
使用左右交换的方法，来操作非重复元素往前排
"""

def removeDuplicates(nums):
    # 先固定左侧第一个数字
    leftnum = nums[0]
    # 第一个交换位置
    idx = 1
    # 从第二个数字开始检查
    for i in range(1,len(nums)):
        # 当与前一个数字不同时，则交换该数字到指定位置
        if nums[i]!=leftnum:
            leftnum = nums[i]
            nums[i], nums[idx] = nums[idx], nums[i]
            idx+=1
    return nums,idx
print removeDuplicates([0,0,1,1,1,2,2,3,3,4])

"""
移除数组中的指定元素
https://leetcode-cn.com/problems/remove-element/
也就是说不能开辟新空间，将非指定元素在前面一次排列，指定的可以排在后面，最后返回非重复的个数
使用左右交换的方法，来操作非指定元素往前排
"""
def removeElement(nums, val):
    idx = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[idx], nums[i] = nums[i], nums[idx]
            idx+=1
    return nums, idx
print removeElement([0,1,2,2,3,0,4,2],2)