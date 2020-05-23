# coding:utf-8
"""
对十进制数 n&(n-1)的用途
是否为2的幂，对应的二进制数中有几个1
"""

def is2mi(n):
    """
    对于二进制数，如果为2的幂，那么它的最高位为1，其余为为0
    此时n-1对应的二进制数，最高位为0其余位为1
    &后均为0
    :param n:
    :return:
    """
    flag = n &(n-1)
    return True if not flag else False

def NumberOf1(n):
    """
    十进制数对应的二进制数有几个1
    :param n:
    :return:
    """
    count = 0
    while n:
        count +=1
        n= n&(n-1)
    return n
