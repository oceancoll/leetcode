# coding:utf-8
def rotate(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    # 以中间水平线为中心，对折，行数为奇数时，中间的奇数行为中心
    for i in range(rows/2):
        for j in range(rows):
            matrix[i][j], matrix[rows-i-1][j] = matrix[rows-i-1][j], matrix[i][j]
    # 以左上角-右下角组成的线为边，对折，只要遍历斜线右上部分即可
    for i in range(rows-1):
        for j in range(i+1, rows):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix

a = [
    [5,1,9,11],
    [2,4,8,10],
    [13,3,6,7],
    [15,14,12,16]
]

print rotate(a)
