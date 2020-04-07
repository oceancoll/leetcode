# coding:utf-8
"""
八皇后问题：
如何能够在 8×8 的国际象棋棋盘上放置八个皇后，使得任何一个皇后都无法直接吃掉其他的皇后？
为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。
"""
# 皇后个数1
n = 8
# 一个解
x = []
# 解的集合
X = []

# 剪枝函数
def conflict(k):
    global x
    # 遍历已经确定的前k-1的值，是否与k行有冲突
    for i in range(k):
        # 上述条件的检验标准：
        # 不能位于同一行已满足条件(queen_list的index)
        # 不能位于同一列：是否有已赋值的value相同
        # 斜线：行数之差与列数之差是否相同
        if x[i] == x[k] or abs(x[i]-x[k]) == k-i:
            return True
    return False

# 入口
def queen(k):
    global n, x, X
    # 边界值
    if k >= n:
        # print x
        X.append(x[:]) # 注意x[:]
    # 对同一行的每一列进行检测
    for i in range(n):
        # 这里不是固定长度的0-1模式，使用append
        x.append(i) # 皇后位于i列，入栈
        # 剪枝，
        if not conflict(k):
            queen(k+1)
        x.pop() # 回溯，出栈

# 打印结果
def show(x):
    global n
    for i in range(n):
        print '. ' * x[i] + 'X ' + '. '*(n-x[i]-1)
queen(0)
print X[0]
show(X[0])
