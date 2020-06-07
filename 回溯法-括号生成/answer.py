# coding:utf-8
"""
数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
    示例：
    输入：n = 3
    输出：[
           "((()))",
           "(()())",
           "(())()",
           "()(())",
           "()()()"
         ]

链接：https://leetcode-cn.com/problems/generate-parentheses
https://leetcode-cn.com/problems/generate-parentheses/solution/dong-hua-yan-shi-22-gua-hao-sheng-cheng-by-user743/
"""
def generate(n):
    """
    n组括号
    根据dfs回溯法
    """
    # 存储结果集
    res = []
    def dfs(left, right, temp):
        """
        left:左括号个数
        right:右括号个数
        temp:临时组合样式
        """
        # 边界值，左侧括号的数量==最大括号组数，且右侧括号的数量==最大括号组数，则满足条件，跳出
        if left==n and right==n:
            res.append(temp)
            return
        # 左侧个数小于最大括号组数 eg:"(("
        if left<n:
            dfs(left+1, right, temp+"(")
        # 右侧个数小于左侧个数，且右侧个数小于最大括号数  eg:"((()"
        if left>right and right<n:
            dfs(left, right+1, temp+")")
    # 起始值
    dfs(0,0,"")
    return res
print generate(3)