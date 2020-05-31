# coding:utf-8
"""
机器人的运动范围
https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
地上有一个m行n列的方格，从坐标 [0,0] 到坐标 [m-1,n-1] 。一个机器人从坐标 [0, 0] 的格子开始移动，
它每次可以向左、右、上、下移动一格（不能移动到方格外），也不能进入行坐标和列坐标的数位之和大于k的格子。
例如，当k为18时，机器人能够进入方格 [35, 37] ，因为3+5+3+7=18。但它不能进入方格 [35, 38]，
因为3+5+3+8=19。请问该机器人能够到达多少个格子？

示例 1：
输入：m = 2, n = 3, k = 1
输出：3

示例 2：
输入：m = 3, n = 1, k = 0
输出：1
"""

class Solution:
    """
    使用回溯法进行遍历
    终止条件：
        当 ① 行列索引越界
        或 ② 数位和超出目标值 k
        或 ③ 当前元素已访问过 时，返回
            0 0 ，代表不计入可达解。
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/dfspython-by-li-jun-yu-3/
    https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/solution/mian-shi-ti-13-ji-qi-ren-de-yun-dong-fan-wei-dfs-b/
    """
    def __init__(self):
        self.count = 0

    def movingCount(self, m, n, k):
        box = [[False for j in range(n)] for i in range(m)]
        def diaget(n):
            """
            获取一个数字的各个位数和
            :param n:
            :return:
            """
            tepsum = 0
            while n:
                tepsum += n % 10
                n /= 10
            return tepsum

        def dfs(i, j, m, n, k):
            """
            dfs回溯
            :param i: 当前横坐标
            :param j: 当前纵坐标
            :param m: 最大行数
            :param n: 最大列数
            :param k: 目标值
            :return:
            """
            # 边界值检查。
            if i < 0 or i >= m or j < 0 or j >= n or diaget(i)+diaget(j)>k:
                return
            if box[i][j] == True:
                return
            # 满足条件
            self.count+=1
            box[i][j] = True
            # 回溯
            dfs(i+1, j, m, n, k)
            dfs(i, j+1, m, n, k)

        for i in range(m):
            for j in range(n):
                dfs(i,j,m,n,k)
                return self.count
s = Solution()
m = 2
n = 3
k = 1
print s.movingCount(m,n,k)