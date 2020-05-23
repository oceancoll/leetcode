# coding:utf-8
# 旋转数组的最小数字
"""
假设按照升序排序的数组在预先未知的某个点上进行了旋转。也就是说一组不重复且排列好顺序的数组，后面的一段旋转到前面了，现在要找出
最小的元素
( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。
你可以假设数组中不存在重复元素。
"""

# 解法一： 从头至尾遍历，当下一个元素大于上一个元素时，即满足条件。复杂度太高

# 解法二：使用二分法.该数组一定是单调底增的，最后一个元素最大。

def findMin(nums):
    # https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/solution/xun-zhao-xuan-zhuan-pai-lie-shu-zu-zhong-de-zui-xi/
    # 只有1个元素
    if len(nums) == 1:
        return nums[0]
    left = 0
    right = len(nums)-1
    # 已经排好序的元素
    if nums[right] > nums[0]:
        return nums[0]
    # 二分法
    while left <= right:
        mid = left + (right-left)/2
        # 间断点
        # 考虑数组为奇偶的问题
        if nums[mid] > nums[mid+1]:
            return nums[mid+1]
        if nums[mid-1] > nums[mid]:
            return nums[mid]
        # 缩小左右区间
        # 当二分中间点大于左侧时，说明还在左区间，left右移缩小范围
        if nums[mid]>nums[left]:
            left = mid + 1
        # 当二分中间点小于右侧时，说明还在右区间，right左移缩小范围
        else:
            right = mid - 1
