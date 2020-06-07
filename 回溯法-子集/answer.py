# coding:utf-8
"""
子集
    给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
示例:
    输入: nums = [1,2,3]
    输出:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
链接：https://leetcode-cn.com/problems/subsets
"""
def subsets(nums):
    # 回溯函数，从第一个点开始
    # 针对于原始数据无重复元素
    def backtrack(first=0, curr=[]):
        # 因为是入口，所以有新进入的值，就会插入
        result.append(curr[:])
        for i in range(first, len(nums)):
            # 入栈
            curr.append(nums[i])
            # 递归
            backtrack(i+1, curr)
            # 出栈
            curr.pop()
    # 存储结果
    result = []
    backtrack()
    return result
print subsets([1,2,3])


"""
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
    说明：解集不能包含重复的子集。
示例:
    输入: [1,2,2]
    输出:
    [
      [2],
      [1],
      [1,2,2],
      [2,2],
      [1,2],
      []
    ]
链接：https://leetcode-cn.com/problems/subsets-ii
"""
def uniqsubsets(nums):
    # 回溯函数，从第一个点开始
    # 针对于原始数据有重复元素
    def backtrack(first=0, curr=[]):
        result.append(curr[:])
        for i in range(first, len(nums)):
            # 对相同数据进行跳出，排除重复元素。设置大于first,避免初始0位
            if i>first and nums[i]==nums[i-1]:
                continue
            curr.append(nums[i])
            backtrack(i+1, curr)
            curr.pop()
    # 先对数据做排列，便于相邻数据去重
    nums.sort()
    result = []
    backtrack()
    return result
print uniqsubsets([1,2,3,3])

