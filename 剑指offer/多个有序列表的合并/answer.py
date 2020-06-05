# coding:utf-8
"""
多个有序列表的合并
通过分治的方法，将数据最终变为两个数组的合并
"""
def mergetwo(l1, l2):
    """
    两个有序数组的合并
    """
    result = []
    while l1 and l2:
        if l1[0]<l2[0]:
            result.append(l1.pop(0))
        else:
            result.append(l2.pop(0))
    if l1:
        result+=l1
    if l2:
        result+=l2
    return result

def mergen(lists):
    """
    多个列表的合并
    """
    count = len(lists)
    if count<2:
        return lists
    def merge(lists, left,right):
        if left==right:
            return lists[left]
        mid = (left+right)/2
        left = merge(lists, left, mid)
        right = merge(lists, mid+1, right)
        return mergetwo(left, right)
    return merge(lists, 0, count-1)
print mergen([[1,3,5],[2,4,6],[2,6,8]])
