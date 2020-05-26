# coding:utf-8
"""
求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句（A?B:C）
https://leetcode-cn.com/problems/qiu-12n-lcof/solution/mian-shi-ti-64-qiu-1-2-nluo-ji-fu-duan-lu-qing-xi-/
"""

class Solution:
    """
    根据递归的思想
    if n==1:return 1
    n+=Sum_Solution(n-1)
    return ct
    因为不能使用if 故使用n>1 and 来判断
    """
    def __init__(self):
        self.cnt=0
    def Sum_Solution(self, n):
        # write code here
        n>1 and self.Sum_Solution(n-1)
        self.cnt+=n
        return self.cnt