# coding:utf-8
"""
以数组 intervals 表示若干个区间的集合，该集合为非排序集合
将具有交集的集合进行组合，并排序返回

事例1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

事例2：
输入：intervals = [[1,4],[0,4]]
输出：[[0,4]]
解释：区间 [1,4] 和 [0,4] 重叠, 将它们合并为 [0,4].
"""

def merge(intervals):
    intervals = sorted(intervals)
    res = []
    for interval in intervals:
        if not res or res[-1][-1]< interval[0]:
            res.append(interval)
        else:
            res[-1][-1] = max(interval[1], res[-1][-1])
    return res
print merge([[1,3],[2,6],[8,10],[15,18]])
