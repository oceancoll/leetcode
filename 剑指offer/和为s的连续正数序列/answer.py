# coding:utf-8
"""
和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
"""

def findContinuousSequence(target):
    """
    和为s的连续正数序列
    https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
    使用滑动窗口法，滑动窗口是一个左闭右开区间
    当窗口的和小于 target 的时候，窗口的和需要增加，所以要扩大窗口，窗口的右边界向右移动
    当窗口的和大于 target 的时候，窗口的和需要减少，所以要缩小窗口，窗口的左边界向右移动
    当窗口的和恰好等于 target 的时候，我们需要记录此时的结果。设此时的窗口为 [i, j)[i,j)，
    那么我们已经找到了一个 ii 开头的序列，也是唯一一个 ii 开头的序列，接下来需要找 i+1i+1 开头的序列，
    所以窗口的左边界要向右移动
    :param target:
    :return:
    """
    i = 1  # 滑动窗口的左边界
    j = 1  # 滑动窗口的右边界
    sumnum = 0  # 滑动窗口中数字的和
    result = []  # 结果
    # 左节点一定小于等于中间值
    while i <= target/2:
        if sumnum < target:
            # 右边界向右移动
            sumnum += j
            j+=1
        elif sumnum > target:
            # 左边界向右移动
            sumnum-=i
            i += 1
        else:
            # 记录结果
            arr = list(range(i,j))
            result.append(arr)
            # 左边界向右移动
            sumnum-=i
            i+=1
    return result
