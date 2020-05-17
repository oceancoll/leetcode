# coding:utf-8
def searchMatrix(matrix, target):
    if not matrix:
        return False
    rows, cols = len(matrix), len(matrix[0])
    # 设置初始值
    row, col = rows-1, 0
    while row>0 and col<cols-1:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col]>target:
            row-=1
        else:
            col+=1
    return False

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5
target1 = 20
print searchMatrix(matrix, target)
print searchMatrix(matrix, target1)