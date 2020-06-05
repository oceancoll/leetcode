# coding:utf-8
"""
分割等和子集
给定一个只包含正整数的非空数组。是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
    示例 1:
        输入: [1, 5, 11, 5]
        输出: true
        解释: 数组可以分割成 [1, 5, 5] 和 [11].
    示例 2:
        输入: [1, 2, 3, 5]
        输出: false
        解释: 数组不能分割成两个元素和相等的子集.
链接：https://leetcode-cn.com/problems/partition-equal-subset-sum
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/416fen-ge-deng-he-zi-ji-by-liucx-3/
https://leetcode-cn.com/problems/partition-equal-subset-sum/solution/pythondong-tai-gui-hua-jian-ji-suan-fa-by-fei-ben-/
"""
class Solution(object):
    def canPartition(self, nums):
        sums,n = sum(nums),len(nums)
        if sums % 2 == 1:
            return False
        target = sums/2
        dp = [[False]*(target+1) for _ in range(n)]
        nums.sort()
        for i in range(n):
            for j in range(nums[i],target+1):
                if nums[i]==j:
                    dp[i][j]=True
                else:
                    dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i]]
        return dp[-1][-1]