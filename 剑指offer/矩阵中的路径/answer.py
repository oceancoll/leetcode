# coding:utf-8
"""
矩阵中的路径
请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。
路径可以从矩阵中的任意一格开始，每一步可以在矩阵中向左、右、上、下移动一格。
如果一条路径经过了矩阵的某一格，那么该路径不能再次进入该格子。
例如，在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字母用加粗标出）。

[["a","b","c","e"],
["s","f","c","s"],
["a","d","e","e"]]

但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。

 

示例 1：

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：

输入：board = [["a","b"],["c","d"]], word = "abcd"
输出：false

"""

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def exists(origin, words):
    """
    https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/solution/java-python3ji-bai-96chao-xiang-xi-jie-ti-guo-chen/
    :param origin:
    :param words:
    :return:
    """
    if not origin:
        return False
    words = list(words)
    # 对所有点进行遍历
    for i in range(len(origin)):
        for j in range((len(origin[0]))):
            # 从第一个点开始
            if dfs(origin, words, i, j, 0):
                return True
    return False

def dfs(origin, words, i, j, index):
    """
    dfs回溯
    :param origin: 原始数组
    :param words: 单词列表
    :param i: 第i行
    :param j: 第j列
    :param index: words的第index位
    :return:
    """
    # 进行边界检查。剪枝。是否在数组内，入口是否与words的index相同
    if i<0 or i>=len(origin) or j<0 or j>=len(origin[0]) or origin[i][j]!=words[index]:
        return False
    # 满足条件，返回
    if len(words)-1==index:
        return True
    # 回溯出栈
    tmp = origin[i][j]
    # 标记
    origin[i][j] = "1"
    # 向下检测，对四个方向进行检查
    is_exist = dfs(origin, words, i, j-1, index+1) or dfs(origin, words, i, j+1, index+1) or dfs(origin, words, i+1, j, index+1) or dfs(origin, words, i-1, j, index+1)
    # 回溯入栈
    origin[i][j] = tmp
    return is_exist
print exists(board, word)
