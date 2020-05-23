# coding:utf-8
"""
调整数组顺序使奇数位于偶数前面

case1:
    调整后左侧是奇数，右侧是偶数

case2:
    调整后左侧是奇数，右侧是偶数，且相对位置与调整前相同
"""
a = [1,2,3,4,5,6,7]
def reOrderArray1(origin):
    # https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/solution/mian-shi-ti-21-diao-zheng-shu-zu-shun-xu-shi-qi-4/
    # 类似于快排的思路，两个指针从两边向中间靠拢
    left = 0
    right = len(origin)-1
    while left < right:
        # 左侧为奇数
        while left < right and origin[left] %2==1:
            left +=1
        # 右侧为偶数
        while left< right and origin[right] %2==0:
            right -=1
        origin[left], origin[right] = origin[right], origin[left]
    return origin
# print reOrderArray1(a)

def reOrderArray2(origin):
    # https://blog.csdn.net/u010005281/article/details/79857035
    # 双指针
    # divP指向左半段已经排好序的“前奇后偶”数组中最后一个奇数的位置；
    # searchP始终位于divP的右边，指向数组右半段中出现的第一个奇数的位置
    divp = 0
    for i in range(len(origin)):
        # 找到奇数，divp之后，i之前均为偶数
        if origin[i]%2==1:
            # searchp指针
            searchp = i
            # 不断的进行前后替换，将奇数换到偶数前面
            while searchp > divp:
                origin[searchp], origin[searchp-1] = origin[searchp-1], origin[searchp]
                searchp -= 1
            # 移动奇数指针
            divp += 1
    return origin

print reOrderArray2(a)
