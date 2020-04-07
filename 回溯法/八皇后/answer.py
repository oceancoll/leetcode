# coding:utf-8
"""
八皇后问题：
如何能够在 8×8 的国际象棋棋盘上放置八个皇后，使得任何一个皇后都无法直接吃掉其他的皇后？
为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。

解题思路：

1、先生成一个规定行数,元素均为None的数组，数组的index分别代表，棋盘的行数，数组的value值代表棋盘的列数，表示皇后处于该行该列

2、对每一行的列进行遍历，同时校验该列如果赋值，与前面以经赋值的数字，是否会有冲突，如果有冲突跳到下一列，如果没冲突，则跳到下一行

链接：https://blog.csdn.net/moqsien/article/details/79588052

"""

def queen(queen_list, current_row=0):
    """
    使用回溯法进行八皇后问题
    :param arr: 皇后所处位置，初始值为[None, None, None, None], 结果为[1, 3, 0, 2]
                所处arr的index为第几行，arr的value为第几列
    :param current_row: 起始行数
    :return: []
    """
    # 设置终止条件，当遍历到最后一行时，退出
    if current_row == len(queen_list):
        print queen_list
        return
    # 对棋盘所在行的列数进行遍历
    for column in range(len(queen_list)):
        # 先预设该列数满足条件，赋值给该行，flag为标志为：该列是否满足八皇后的要求条件
        queen_list[current_row], flag = column, True
        # 对已赋值行数的值，进行与该行的值进行校验，即任意两个值不能在同一行，同一列，不能位于同一斜线
        for row in range(current_row):
            # 上述条件的检验标准：
            # 不能位于同一行已满足条件(queen_list的index)
            # 不能位于同一列：是否有已赋值的value相同
            # 斜线：行数之差与列数之差是否相同
            if queen_list[row] == column or (abs(queen_list[row] - column) == current_row - row):
                # 如果满足条件，说明不符合，flag=flase
                flag = False
                # 跳出校验，对下一列进行判断
                break
        # 如果flag为True,说明该列满足条件，则跳到下一行的赋值
        if flag:
            queen(queen_list, current_row + 1)

queen([None]*8)