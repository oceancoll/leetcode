# coding:utf-8
"""
0-1背包问题：
有一批货物，分别有重量和对应的价值
有一个背包有最大装载量，在一个货物最多只能装1次的条件下，满足最大装载量的条件下，使得背包装载货物的价值最大
"""

n = 3             # 物品数量
c = 30            # 包的载重量
w = [20, 15, 15]  # 物品重量
v = [45, 25, 25]  # 物品价值

maxw = 0          # 合条件的能装载的最大重量
maxv = 0          # 合条件的能装载的最大价值
bag = [0, 0, 0]   # 一个解（n元0-1数组）长度固定为n
bags = []         # 一组解
bestbag = None    # 最佳解


# 计算当前背包的重量
def get_a_pack_weight(bag):
    global w
    return sum([w[m] for m,n in enumerate(bag, 0) if n==1])


# 计算当前背包的价值
def get_a_pack_value(bag):
    global v
    return sum([v[m] for m,n in enumerate(bag, 0) if n==1])


# 剪枝函数
def conflict(k):
    global bag, c, w
    # 前k件物品的重量是否小于背包的最大可载重量
    if sum([w[i] for i in range(k+1) if bag[i]==1]) > c:
        return True
    return False


# 入口
def backpack(k):
    global n, bag, maxw, maxv, bestbag
    # 边界值
    if k >=n:
        # 对于有最优解的情况，需要再判断一下与其他解的关系，选出最优解
        cw = get_a_pack_weight(bag)  # 当前背包的重量
        cv = get_a_pack_value(bag)   # 当前背包的价值
        # 当前价值较大
        if cv > maxv:
            maxv = cv
            bestbag = bag[:]
        # 价值相同，重量更小
        if cv == maxv and cw < maxw:
            maxw = cw
            bestbag = bag[:]
    else:
        # 对于解的长度固定的情况，使用[1,0]解，x[k]=1的方式
        for i in [1,0]:
            bag[k] = i
            # 剪枝函数
            if not conflict(k):
                # 继续检测下一位
                backpack(k+1)
backpack(0)
print bestbag
print get_a_pack_weight(bestbag)
print get_a_pack_value(bestbag)