# coding:utf-8
"""
将一个数字n变为m个数字和，使得这m个数字的乘积最大
https://leetcode-cn.com/problems/integer-break/solution/gai-yong-chu-fa-ji-suan-chu-3de-ge-shu-by-mnm135/
3越多乘积越大
所以对n与3相除，根据余数情况判断
余数为1时，（商-1）* 4，因为3*1<2*2
余数为2,直接相乘
余数为0，直接相乘
"""

def integerBreak(n):
    if n<4:
        return n-1
    a,b = divmod(n,3)
    if b==1:
        return 3**(a-1)*4
    elif b==2:
        return 3**a*2
    else:
        return 3**a
