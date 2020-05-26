# coding:utf-8
"""
扑克牌中的顺子

从扑克牌中随机抽5张牌，判断是不是一个顺子，即这5张牌是不是连续的。
2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

输入: [1,2,3,4,5]
输出: True

简单而言：
https://leetcode-cn.com/problems/bu-ke-pai-zhong-de-shun-zi-lcof/solution/mian-shi-ti-61-bu-ke-pai-zhong-de-shun-zi-ji-he-se/
1.除0外无重复的数字
2.除0外，最大值与最小值差差小于5
"""

def IsContinuous(numbers):
    dic = set()
    minnum = 14
    maxnum = -1
    for i in numbers:
        if i == 0:
            continue
        if i in dic:
            return False
        else:
            if i<minnum:
                minnum = i
            if i>maxnum:
                maxnum = i
            if maxnum-minnum >=5:
                return False
            dic.add(i)
    return True