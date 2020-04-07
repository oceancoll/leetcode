# coding:utf-8
"""
给定一个迷宫，入口已知。出口为迷宫边缘上除了入口以外的0点
问是否有路径从入口到出口，若有则输出一条这样的路径。
注意移动可以从上、下、左、右、上左、上右、下左、下右八个方向进行。
迷宫输入0表示可走，输入1表示墙。为方便起见，用1将迷宫围起来避免边界问题。



考虑到左、右是相对的，
因此修改为：北、东北、东、东南、南、西南、西、西北八个方向。
在任意一格内，有8个方向可以选择，亦即8种状态可选。
因此从入口格子开始，每进入一格都要遍历这8种状态。

显然，可以套用回溯法的子集树模板。

注意，解的长度是不固定的。

八种可选走法的图片
https://images2015.cnblogs.com/blog/709432/201705/709432-20170529231250305-2021787932.png
"""
import copy
# 迷宫（1是墙，0是通路）
maze = [[1,1,1,1,1,1,1,1,1,1],
        [0,0,1,0,1,1,1,1,0,1],
        [1,1,0,1,0,1,1,0,1,1],
        [1,0,1,1,1,0,0,1,1,1],
        [1,1,1,0,0,1,1,0,1,1],
        [1,1,0,1,1,1,1,1,0,1],
        [1,0,1,0,0,1,1,1,1,0],
        [1,1,1,1,1,0,1,1,1,1]]
m, n = 8, 10    # 8行，10列
entry = (1,0)   # 迷宫入口
path = [entry]  # 一个解（路径）
paths = []      # 一组解
# 移动的方向（顺时针8个：N, EN, E, ES, S, WS, W, WN）
directions = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]

# 剪枝方法
def conflict(nx, ny):
    # 是否在迷宫中，以及是否可通行
    if 0 <= nx < m and 0<= ny < n and maze[nx][ny] == 0:
        return False
    return True

# 入口
def walk(x, y): # 到达(x,y)格子
    global entry, m, n, directions, maze
    # 跳出条件，1、不为入口，2、位于最右侧的列或者最下面的行
    if (x, y) != entry and (x % (m-1) ==0 or y%(n-1)==0):
        # print path
        paths.append(path[:])
    else:
        # 遍历8个方向(亦即8个状态)
        for d in directions:
            # 选取待走一步后的坐标位置
            nx, ny = x+d[0], y+d[1]
            # 因为长度不确定，故使用append方法
            # 保存，新坐标入栈
            path.append((nx,ny))
            # 剪枝方法
            if not conflict(nx, ny):
                # 如果可行，标记，已访问
                maze[nx][ny] = 2
                # 向下进行
                walk(nx, ny)
                # 回溯，恢复，这里需要回溯的原因是，上面修改了原始值
                maze[nx][ny] = 0
            # 回溯，出栈
            path.pop()

# 展示方法
def show(path):
    global maze
    maze2 = copy.deepcopy(maze)
    for x,y in path:
        maze2[x][y] = 2
    print '------原迷宫--------'
    for i in maze:
        print i
    print '------现迷宫--------'
    for i in maze2:
        print i
walk(1,0)
show(paths[1])