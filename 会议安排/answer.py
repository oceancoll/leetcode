# coding:utf-8
"""
二维数组，表示会议的开始和结束时间。每场会议需要一个主持人，每个主持人同时只能主持一场会议
最少需要几个主持人
输入：[[1,2],[2,3]]
输出：1

输入：2,[[1,3],[2,4]]
输出：2
"""
def minmumNumberOfHost(startEnds):
    start = []
    end = []
    count = len(startEnds)
    for i in startEnds:
        start.append(i[0])
        end.append(i[1])
    res = 0
    index = 0
    for i in range(count):
        if start[i]>=end[index]: # 开始的时间大于结束的时间，说明这条已经被算过了
            index+=1
        else:
            res+=1
    return res

"""
二位数组，表示：多场演唱会的开始和结束时间
从某时刻开始有时间，一共可以最多参与多少场
输入：[Node(6,8), Node(7,9), Node(6.5,8.5), Node(9.5,11), Node(10,10.5), Node(10.4,12)]， start=6
输出：2 // 最多参加两场
"""
class Node(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

def bestArrange(programs, start_time):
    # 根据结束时间进行排序
    programs = sorted(programs, key = lambda x: x.end)
    res = 0
    for i in range(len(programs)):
        if start_time<=programs[i].start:
            res+=1
            start_time = programs[i].end
    return res
programs = [Node(6,8), Node(7,9), Node(6.5,8.5), Node(9.5,11), Node(10,10.5), Node(10.4,12)]
print bestArrange(programs, 6)
