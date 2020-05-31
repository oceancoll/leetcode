# coding:utf-8
"""
二分查找
对于一个已经排好序的列表，通过二分查找的方式，找到对应的数
1. 数值均不重复
2. 找到最左侧的
3. 找到最右侧的
"""
nums = [1,3,3,3,4,5]
target = 4
def erfen1(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:  # 相遇时仍需检测
        mid = (left+right)/2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1  # mid已经检查
        else:
            left = mid + 1
    return -1
# print erfen1(nums, target)

def erfen2(nums, target):
    # 最左侧
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)/2
        if nums[mid] == target:
            right = mid -1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # 边界值检查，left的取值范围为[0,len(nums)]
    if left>=len(nums) or nums[left] != target:
        return -1
    return left
# print erfen2(nums, 3)


def erfen3(nums, target):
    # 最右侧
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) / 2
        if nums[mid] == target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # 边界值检查，right[-1,len(nums)-1]
    if right < 0 or nums[right] != target:
        return -1
    return right
print erfen3(nums, 3)


