# coding:utf-8

"""
我们把只包含因子 2、3 和 5 的数称作丑数（Ugly Number）。求按从小到大的顺序的第 n 个丑数
其中1也为丑数。也就是说分解因式后只包含这些数字的数被称为丑数
"""

def isugly(n):
    """
    判断一个数是否是丑数
    :param n:
    :return:
    """
    while n%2==0:
        n/=2
    while n%3==0:
        n/=3
    while n%5==0:
        n/=5
    if n==1:
        return True
    else:
        return False
print isugly(8)

def uglynums(n):
    """
    获取前n个丑数
    采用指针的方式
    :param n:
    :return:
    """
    if n<=0:
        return []
    nums = [1]
    p1,p2,p3=0,0,0
    while len(nums)<n:
        # 选取当前轮最小数
        tmp = min(nums[p1]*2, nums[p2]*3, nums[p3]*5)
        nums.append(tmp)
        if tmp % 2 ==0:
            p1+=1
        if tmp % 3==0:
            p2+=1
        if tmp%5==0:
            p3+=1
    return nums
print uglynums(10)
