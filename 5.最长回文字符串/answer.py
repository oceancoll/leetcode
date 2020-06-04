# coding:utf-8
"""
最长回文子字符串
    给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

示例 1：
    输入: "babad"
    输出: "bab"
    注意: "aba" 也是一个有效答案。

示例 2：
    输入: "cbbd"
    输出: "bb"
"""

def longestPalindrome(s):
    """
    最长回文字符串
    固定一个点向两边扩散的方法
    https://leetcode-cn.com/problems/longest-palindromic-substring/solution/hui-wen-wen-ti-dong-tai-gui-hua-jspython5-zui-chan/
    :param s:
    :return:
    """
    # 扩散函数
    def extend(left, right, s):
        while (left>=0 and right<len(s) and s[left]==s[right]):
            left-=1
            right+=1
        return s[left+1:right]

    n = len(s)
    if n==0:
        return ""
    # 最小值兜底
    res = s[0]
    for i in range(n-1):
        # 针对奇偶情况向两边扩散
        e1 = extend(i,i,s)
        e2 = extend(i,i+1,s)
        # 判断奇偶对应长度和记录最大长度的关系
        if max(len(e1), len(e2))>len(res):
            res = e1 if len(e1) >len(e2) else e2
    return res

print longestPalindrome("babad")