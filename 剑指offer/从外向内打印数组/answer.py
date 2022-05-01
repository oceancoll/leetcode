# coding:utf-8
"""
顺时针从外向内打印数组

01 02 03 04
05 06 07 08
09 10 11 12
13 14 15 16
需要依次打印出1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.

"""
def printMatrix(matrix):
    result = []
    x0,y0 = 0,0
    xn,yn = len(matrix)-1, len(matrix[0])-1
    while x0<=xn and y0<=yn:
        # 从左到右
        for i in range(y0, yn+1, 1):
            result.append(matrix[x0][i])
        # 从上到下
        for i in range(x0+1, xn+1, 1):
            result.append(matrix[i][yn])
        # 针对非n*n数组，比如单行
        if x0<xn:
            # 从右到左
            for i in range(yn-1, y0-1, -1):
                result.append(matrix[xn][i])
        if y0<yn:
            # 从下到上
            for i in range(xn-1, x0, -1):
                result.append(matrix[i][y0])
        x0+=1
        y0+=1
        xn-=1
        yn-=1
    return result
a = [[1,2,3,4],
     [5,6,7,8],
     [9,10,11,12],
     [13,14,15,16]
     ]
a= [[1],[2],[3],[4],[5]]
print printMatrix(a)