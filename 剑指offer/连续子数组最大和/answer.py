# coding:utf-8
"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和
输入: [-2,1,-3,4,-1,2,1,-5,4],
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6
"""

def FindGreatestSumOfSubArray(origin):
    # 以第一个值为最大值
    currsum, maxsum = origin[0], origin[0]
    # 从第二个数开始向上累加
    for num in origin[1:]:
        # 当前值大于0时继续累加，否则变为当前值
        currsum = currsum+num if currsum>0 else num
        # 取最大值
        maxsum = currsum if currsum>maxsum else maxsum
    return maxsum
