# coding:utf-8
"""
0,1,,n-1这n个数字排成一个圆圈，从数字0开始，
每次从这个圆圈里删除第m个数字。求出这个圆圈里剩下的最后一个数字。

例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，
则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

pos=(pos+step)%num
"""

def lastRemaining(m,n):
    """
    m 为数字个数
    n 为步长
    思想：从后往前推
    https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/zhe-huo-xu-shi-ni-neng-zhao-dao-de-zui-xiang-xi-yu/
    :param m:
    :param n:
    :return:
    """
    if m<1:
        return -1
    pos = 0  # 代表了最后结果只剩下了 1 个数字，这个数字处于第 0 个位置
    i = 2  # 循环从数组长度有 2 个开始，即从剩下了两个数字开始计算
    while i<=n:  # 循环到数组中剩下 n 个人结束，即到达了题目要求的那么多数字，此时的 pos 就是最后剩下的那个数字的在 n 个数字中位置。
        pos = (pos+n)%i
        i+=1
    return pos
