# coding:utf-8
"""
在排序数组中查找目标元素出现的第一个和最后一个位置
https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
根据二分法，先查最左侧的边界值，再查最右侧的边界值
"""
def searchRange(nums, target):
    count = len(nums)
    left = 0
    right = count - 1
    # 设置默认值
    result = [-1, -1]
    # 检测最左边界值
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            right = mid - 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    result[0] = left if left < count and nums[left] == target else -1
    # 如果左边界值不存在，说明该数不存在，则跳出
    if result[0] == -1:
        return result
    # 重新赋值左右边界
    left = 0
    right = count - 1
    # 检测最右边界值
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    result[1] = right if right >= 0 and nums[right] == target else -1
    return result

a = [5,7,7,8,8,10]
print searchRange(a, 5)
print searchRange(a, 8)