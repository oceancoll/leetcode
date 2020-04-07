# ccoding:utf-8

"""
0-1背包问题：
有一批货物，分别有重量和对应的价值
有一个背包有最大装载量，在一个货物最多只能装1次的条件下，满足最大装载量的条件下，使得背包装载货物的价值最大

解题思路：


链接：https://blog.csdn.net/qq_34497812/article/details/69488016
     https://blog.csdn.net/weixin_30642869/article/details/99396359
"""

class BackSack():
    """
    使用回溯法进行0-1背包问题
    """

    def __init__(self, bagmaxweight):
        # 背包最大装载重量
        self.bagmaxweight = bagmaxweight
        # 背包当前重量
        self.bagcurrentweight = 0
        # 背包当前价值
        self.bagcurrentvalue = 0
        # 背包最优解货物
        self.bestgoods = []
        # 背包最优解重量
        self.bestweight = 0
        # 背包最优解价值
        self.bestvalue = 0

    # 计算函数
    def cal(self, i):
        global goodsnum, nullgoods, goodsweight, goodsvalue
        # 边界值，计算到最后一位时跳出
        if i == goodsnum:
            # 当背包当前价值>最优价值时
            if self.bagcurrentvalue > self.bestvalue:
                # 用当前重量和价值替换最优重量和价值
                self.bestweight = self.bagcurrentweight
                self.bestvalue = self.bagcurrentvalue
                # 最优货物==标志的位货物
                self.bestgoods = nullgoods[:goodsnum]
            return
        # 当前背包重量+遍历到的货物重量<=背包最大装载量时
        if self.bagcurrentweight+goodsweight[i] <= self.bagmaxweight:
            # 将该位置的值置为1
            nullgoods[i] = 1
            # 将当前重量和价值都增加
            self.bagcurrentweight += goodsweight[i]
            self.bagcurrentvalue += goodsvalue[i]
            # 后移一位，对后面的数据进行检测
            self.cal(i+1)
            # 交换完以后，恢复交换前的状态
            self.bagcurrentweight -= goodsweight[i]
            self.bagcurrentvalue -= goodsvalue[i]
            nullgoods[i] = 0
        # 当该节点不满足时，跳到下一位
        self.cal(i+1)

# 背包最大装载重量
bagmaxweight = 10
# 物品的重量
goodsweight=[2,2,6,5,4]
# 物品的价值
goodsvalue=[6,3,5,4,6]
# 物品的数量
goodsnum = len(goodsweight)
# 用来标志物品是否携带的空数组,0为不携带，1为携带，index对应物品的位置
nullgoods =[0]*goodsnum
# 初始化方法
backsack = BackSack(bagmaxweight)
# 从第0位开始
backsack.cal(0)
# 输出最优解
print backsack.bestgoods