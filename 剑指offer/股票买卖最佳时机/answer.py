# coding:utf-8

"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
"""

def maxProfit(prices):
    # 不断去遍历数字，并检查该数字后是否有大于该数字的数字，如果有则差值与max进行比较
    maxprofits = 0
    for i in range(len(prices)-1):
        currdata = prices[i]
        biggerdata = max(prices[i:])
        if biggerdata > currdata and biggerdata-currdata>maxprofits:
            maxprofits = biggerdata-currdata
    return maxprofits

