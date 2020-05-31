# coding:utf-8
"""
给你一个包含 n 个整数的数组 nums，
判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例：
给定数组 nums = [-1, 0, 1, 2, -1, -4]，
满足要求的三元组集合为：
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
"""
def threesum(nums, target):
    """
    先排序
    通过固定第一个值，对后两个值进行双指针计算
    对于相邻两个值相同的情况，直接跳过，减少遍历次数，避免重复值
    """
    nums = sorted(nums)
    count = len(nums)
    result = []
    for i in range(count):
        # 从第二个值开始判断是否与前一个值相同，从而进行剪枝
        if i>0 and nums[i]==nums[i-1]:
            continue
        # 设置双指针，类似于二个数字求和,分别从左到右，和从右到左
        left =i+1
        right = count-1
        while left < right:
            # 满足条件的情况
            if nums[i] + nums[left] + nums[right] == target:
                result.append([nums[i],nums[left],nums[right]])
                # 对于相邻数相同的情况可以直接跳过
                while left<right and nums[left] == nums[left+1]:
                    left +=1
                while left<right and nums[right] == nums[right-1]:
                    right -=1
                left+=1
                right-=1
            elif nums[i] + nums[left] + nums[right] > target:
                right-=1
            else:
                left+=1
    return result
#print threesum([-1, 0, 1, 2, -1, -4], 0)


"""
四数之和
给定一个包含 n 个整数的数组 nums 和一个目标值 target，
判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c + d 的值与 target 相等？
找出所有满足条件且不重复的四元组。

注意：
答案中不可以包含重复的四元组。

示例：
给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。

满足要求的四元组集合为：
    [
      [-1,  0, 0, 1],
      [-2, -1, 1, 2],
      [-2,  0, 0, 2]
    ]
"""

def foursum(nums, target):
    count = len(nums)
    nums = sorted(nums)
    result = []
    # 固定第一个数
    for i in range(count):
        # 当与前一个数相同时跳过
        if i > 0 and nums[i] == nums[i-1]:
            continue
        # 固定第二个数，基于第一位
        for j in range(i+1, count):
            # 当与前一个数相同时跳过
            if j> i+1 and nums[j] == nums[j-1]:
                continue
            # 第三、第四个数调整
            left = j + 1
            right = count-1
            while left < right:
                if nums[i]+nums[j]+nums[left]+nums[right]==target:
                    result.append([nums[i],nums[j],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right] == nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[i]+nums[j]+nums[left]+nums[right]>target:
                    right-=1
                else:
                    left+=1
    return result
print foursum(nums=[1, 0, -1, 0, -2, 2], target = 0)