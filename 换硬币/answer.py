# coding:utf-8
"""
有几种不同面额的硬币，使用更大额的钱，来换硬币，是否可以换，可以换几个
如果可以换，输出换的个数，如果不能换，返回-1
输入：[5,2,3],20
输出：4 // 可以换4个5

输入：[5,2,3],0
输出：0 // 不用换

输入：[3,5],2
输出：-1 // 无法换

https://blog.csdn.net/sjq_915/article/details/108910004
dp思想，不断尝试
"""
def minMoney(nums, target):
    maxnum = float("+inf")
    dp = [[0 for _ in range(target+1)]for _ in range(len(nums))]
    for i in range(target+1):
        a,b = divmod(i, nums[0])
        if b==0:
            dp[0][i] = a
        else:
            dp[0][i] = maxnum
    for i in range(1, len(nums)):
        for j in range(target + 1):
            tmp = maxnum
            if j-nums[i]>=0 and dp[i][j-nums[i]] != maxnum:
                tmp = dp[i][j-nums[i]] + 1
            dp[i][j] = min(tmp, dp[i-1][j])

    return dp[-1][-1] if dp[-1][-1] != maxnum else -1

print minMoney([5,2,3], 10)

