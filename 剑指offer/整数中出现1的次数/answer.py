# coding:utf-8
"""
整数中出现1的次数
"""

def NumberOf1Between1AndN_Solution(n):
    # https://leetcode-cn.com/problems/number-of-digit-one/solution/python-tong-su-yi-dong-jie-fa-by-blaoke/
    maxlen = len(str(n))
    count = 0
    for i in range(maxlen):
        diagit = 10 ** i
        low = n % diagit
        high = n / (diagit * 10)
        curr = (n / diagit) % 10
        if curr == 0:
            count += high * diagit
        elif curr == 1:
            count += high * diagit + low + 1
        else:
            count += high * diagit + diagit
    return count
