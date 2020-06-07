# coding:utf-8
"""
33. 搜索旋转排序数组
    假设按照升序排序的数组在预先未知的某个点上进行了旋转。
    ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
你可以假设数组中不存在重复的元素。
你的算法时间复杂度必须是 O(log n) 级别。
    示例 1:
        输入: nums = [4,5,6,7,0,1,2], target = 0
        输出: 4
    示例 2:
        输入: nums = [4,5,6,7,0,1,2], target = 3
        输出: -1
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/
https://leetcode-cn.com/problems/search-in-rotated-sorted-array/solution/sou-suo-xuan-zhuan-pai-xu-shu-zu-by-powcai/
"""
def search(nums, target):
    """
    二分法解决
    :param nums:
    :param target:
    :return:
    """
    count = len(nums)
    left = 0
    right = count-1
    while left<right:
        mid = (left+right)/2
        # 相同时
        if nums[mid]==target:
            return mid
        # mid大于左侧节点时，说明mid位于左侧
        elif nums[mid] >= nums[left]:
            # 当target在左区间时
            if nums[left]<= target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        # mid位于右侧
        else:
            # 当target位于右区间时
            if nums[mid]<target<=nums[right]:
                left = mid+1
            else:
                right = mid-1
    # 判断left的值是否等于target
    return left if nums[left]==target else -1
print search([4,5,6,7,0,1,2],0)