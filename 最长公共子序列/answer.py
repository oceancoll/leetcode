# coding:utf-8
"""
1143. 最长公共子序列

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。
一个字符串的 子序列 是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。
例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的「公共子序列」是这两个字符串所共同拥有的子序列。
若这两个字符串没有公共子序列，则返回 0。

示例 1:
    输入：text1 = "abcde", text2 = "ace"
    输出：3
    解释：最长公共子序列是 "ace"，它的长度为 3。
示例 2:
    输入：text1 = "abc", text2 = "abc"
    输出：3
    解释：最长公共子序列是 "abc"，它的长度为 3。
示例 3:
    输入：text1 = "abc", text2 = "def"
    输出：0
    解释：两个字符串没有公共子序列，返回 0。

链接：https://leetcode-cn.com/problems/longest-common-subsequence
https://leetcode-cn.com/problems/longest-common-subsequence/solution/python-xiao-lu-yi-ban-dan-shi-sheng-zai-jian-duan-/
"""
def longestCommonSubsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]
text1 = "abcde"
text2 = "ace"
print longestCommonSubsequence(text1, text2)

def longestCommonSubsequenceWithResult(text1, text2):
    """
    返回最长公共子序列实际的结果，需要将字符保存在dp中
    """
    m = len(text1)
    n = len(text2)
    dp = [['' for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + text1[i-1]
            else:
                if len(dp[i-1][j])>len(dp[i][j-1]):
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i][j-1]
    return dp[m][n]
print longestCommonSubsequenceWithResult("9A8C7D6B54","B9D87A654A")

"""
最长公共字串
和最长公共子序列相比，是中间不能截断，需要是连续的字符串
思路同上：均使用dp，但因为不能截断，因此只要判断两个字符串相同的情况即可

输入："1AB2345CD","12345EF"
输出："2345"
"""
def Lcs(text1, text2):
    m = len(text1)
    n = len(text2)
    maxlen = 0  # 用于记录最长的字符长度
    index = 0  # 用于记录最后一次相同字符串的位置
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if text1[i-1]==text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if maxlen<dp[i][j]:
                    maxlen = dp[i][j]
                    index = i
    if maxlen == 0:
        return ""
    else:
        return text1[index-maxlen:index]
print Lcs("1AB2345CD","12345EF")