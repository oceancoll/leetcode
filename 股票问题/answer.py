# coding:utf-8
"""
股票问题

1. LeetCode 121：最多进行 1 笔交易（k=1）【贪心】 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock
2. LeetCode 122：不限交易次数（k=+inf）【二维 DP】https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii
    3. LeetCode 309：不限交易次数（k=+inf），但有「冷冻期」的额外条件 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown
    4. LeetCode 714：不限交易次数（k=+inf），但有「手续费」的额外条件 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee
5. LeetCode 123：最多进行 2 笔交易（k=2）【三维 DP】https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii
    6. LeetCode 188：最多进行 k 次交易 https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iv
"""

def maxProfit1(prices):
    """
    该位置的与该位置的左侧最小值的差
        input: [7,1,5,3,6,4]
        output: 5

        input: [7,6,4,3,1]
        output: 0
    """
    count = len(prices)
    maxsum = 0
    for i in range(1,count):
        if prices[i]-min(prices[:i])>maxsum:
            maxsum = prices[i]-min(prices[:i])
    return maxsum


def maxProfit2(prices):
    """
    状态转移方程
        Case 1，今天我没有股票，有两种可能：
            昨天我手上就没有股票，今天不做任何操作（rest）；
            昨天我手上有一只股票，今天按照时价卖掉了（sell），收获了一笔钱
        Case 2，今天持有一只股票，有两种可能：
            昨天我手上就有这只股票，今天不做任何操作（rest）；
            昨天我没有股票，今天按照时价买入一只（sell），花掉了一笔钱
    边界状态
        观察状态转移方程，第 i 天的状态只由第 i-1 天状态推导而来，因此边界状态只需要定义 i=0（也就是第一天）即可：
            dp[0][0] = 0        # 第一天没有股票，说明没买没卖，获利为0
            dp[0][1] = -prices[0]   # 第一天持有股票，说明买入了，花掉一笔钱
    """
    count = len(prices)
    # dp[i][j]: i代表天，j(0,1)代表是否持有股票，0未持有，1持有。所对应的值为价值数
    dp = [[None, None] for _ in range(count)]
    # 对第一天的情况进行初始化
    dp[0][0] = 0  # 未持有的情况
    dp[0][1] = -prices[0]  # 持有的情况
    for i in range(1, count):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])  # 当天未持有时：前一天未持有 或 前一天持有今天卖掉
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])  # 当天持有时：前一天持有 或 前一天未持有今天买入
    return dp[-1][0]  # 返回最后一次未持有时的值

def maxProfit3(prices):
    """
    有冷冻期的情况，对于新的一次买入，要么为第一次买入，要么上一次卖出距离现在有一次的间距
    :param prices:
    :return:
    """
    count = len(prices)
    if count<=1:
        return 0
    dp = [[None, None] for _ in range(count)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    dp[1][0] = max(dp[0][0], dp[0][1]+prices[1])  # 昨天就没有 或者 昨天买入今天卖出
    dp[1][1] = max(dp[0][1], dp[0][0]-prices[1])  # 昨天就有 或者 昨天没有而今天买入
    for i in range(2,count):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
        dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])  # 买入股票时注意冷冻期
    return dp[-1][0]

def maxProfit4(prices, fee):
    """
    卖出时有手续费，则在卖出时减去手续费
    :param prices:
    :param fee:
    :return:
    """
    count = len(prices)
    dp = [[None, None]for _ in range(count)]
    dp[0][0] = 0
    dp[0][1] = -prices[0]
    for i in range(1, count):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i]-fee)  # 卖出时扣除手续费
        dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
    return dp[-1][0]

def maxProfit5(prices):
    """
    最多进行 2 笔交易（k=2）
    三维dp,第一个值是天数，第二个值交易次数，第三个值钱数
    :param prices:
    :param k:
    :return:
    """
    count = len(prices)
    dp = [[[None, None] for _ in range(2+1)] for _ in range(count)]
    # 清除边界值
    # 1.j=0时对i穷举;
    # 2.i=0时对有效的j穷举(j=1,2)
    for i in range(count):
        dp[i][0][0] = 0
        dp[i][0][1] = float('-inf')
    for j in range(1, 2+1):
        dp[0][j][0] = 0
        dp[0][j][1] = -prices[0]
    # 状态转移
    for m in range(1, count):
        for n in range(1,2+1):
            dp[m][n][0] = max(dp[m-1][n][0], dp[m-1][n][1]+prices[m])
            dp[m][n][1] = max(dp[m-1][n][1], dp[m-1][n-1][0]-prices[m])
    return dp[-1][-1][0]
print maxProfit5([3,3,5,0,0,3,1,4])


def maxProfit5(prices, k):
    count = len(prices)
    # 当k大于等于一半时，退化为不限次数的交易
    if k>=count/2:
        dp = [[None, None]for _ in range(count)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, count):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1]+prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0]-prices[i])
        return dp[-1][0]
    else:
        dp = [[[None,None]for _ in range(k+1)]for _ in range(count)]
        for i in range(count):
            dp[i][0][0] = 0
            dp[i][0][1] = float('-inf')
        for j in range(1, k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]
        for m in range(count):
            for n in range(1, k+1):
                dp[m][n][0] = max(dp[m-1][n][0], dp[m-1][n][1]+prices[m])
                dp[m][n][1] = max(dp[m-1][n][1], dp[m-1][n-1][0]-prices[m])
        return dp[-1][-1][0]



















