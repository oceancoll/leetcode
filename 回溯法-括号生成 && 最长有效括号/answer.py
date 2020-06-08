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


"""
32. 最长有效括号
    给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
示例 1:
    输入: "(()"
    输出: 2
    解释: 最长有效括号子串为 "()"
示例 2:
    输入: ")()())"
    输出: 4
    解释: 最长有效括号子串为 "()()"

链接：https://leetcode-cn.com/problems/longest-valid-parentheses
https://leetcode-cn.com/problems/longest-valid-parentheses/solution/xiao-bai-du-neng-kan-dong-de-dong-tai-gui-hua-si-l/
"""
def longestValidParentheses(s):
    """
    通过栈的方式来判断长度
    从左到右
        1. 当为"("时入栈
        2. 当为")"时出栈
            a. 出栈后，stack为空时，入栈
            b. 出栈后，stack不为空时，判断当前记录的最长值与，当前index和stack的最后一位相减的长度
    根本是第一位用-1,减法等于+1，避免了list索引从0开始的问题。然后每组成一组()，则stack删除这两个值
    """
    stack = [-1]
    result = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if not stack:
                stack.append(i)
            else:
                result = max(result, i-stack[-1])
    return result
print longestValidParentheses(")()())")