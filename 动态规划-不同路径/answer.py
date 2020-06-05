# coding:utf-8
"""
一个机器人位于m*n的左上角，要到右下角去，一共有多少种方法
"""
def uniquePaths(m,n):
    """
    使用动态规划的方法，记录到达每一个点的有多少种不同方法
    则某点的多少种方法等于，该点上面点的方法次数+左边点的方法此次
    最后右下角的点对应的次数，即为总的次数
    """
    result = [[1 for _ in range(n)] for _ in range(m)]
    # 因为左上角是起始点，所以从非左上角的点开始
    for i in range(1,m):
        for j in range(1,n):
            result[i][j] = result[i-1][j]+ result[i][j-1]
    return result[-1][-1]
print uniquePaths(3,2)==3

