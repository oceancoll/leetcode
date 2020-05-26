# coding:utf-8

"""
输入一个正整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个
输入: [10,2]
输出: "102"

输入: [3,30,34,5,9]
输出: "3033459"
"""

def minNumber(origin):
    """
    先将数字转为字符串，然后进行排序
    前两个正向和大于负向和则为1
    https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
    :param origin:
    :return:
    """
    def sortnums(x,y):
        a, b = x+y, y+x
        if a>b:
            return 1
        elif a<b:
            return -1
        else:
            return 0
    strnums = [str(i) for i in origin]
    strnums = sorted(strnums, cmp=sortnums)
    return ''.join(strnums)
