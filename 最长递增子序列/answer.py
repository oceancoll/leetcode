# coding:utf-8
"""
给定一个数组，找出最长递增的子序列
输入：[2,1,5,3,6,4,8,9,7]
输出：[1,3,4,8,9]
"""

# 满足上述条件的最长个数
def LIS(nums):
    if not nums:
        return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
print LIS([2,1,5,3,6,4,8,9,7])

# 满足上述条件的子序列
def LISA(nums):
    nums = [str(i) for i in nums]
    if not nums:
        return ''
    dp = []
    for i in range(len(nums)):
        dp.append(nums[i])
        for j in range(i):
            if nums[i]>nums[j]:
                if len(dp[i])>len(dp[j])+1:
                    dp[i] = dp[i]
                else:
                    dp[i] = dp[j]+nums[i]
    dp = sorted(dp, cmp=lambda x,y:-1 if len(x)>len(y) else 1)
    return dp[0]
print LISA([2,1,5,3,6,4,8,9,7])

