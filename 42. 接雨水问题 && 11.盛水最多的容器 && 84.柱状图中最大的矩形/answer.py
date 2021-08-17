# coding:utf-8
"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
计算按此排列的柱子，下雨之后能接多少雨水。

<img>https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/22/rainwatertrap.png</img>
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，
在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

示例:
    输入: [0,1,0,2,1,0,1,3,2,1,2,1]
    输出: 6
"""
def trap(height):
    """
    按照列的高度来接雨水
    此种方法的核心思路在于下雨后水能达到的最高位置等于两边最大高度的
    较小值减去当前高度的值，这是按照列来接雨水时的核心思想。
    所以按照列来接雨水的核心问题在于：如何求出左侧的最大值和右侧的最大值
    使用双指针的方法，不断计算左右最大高度。对于较小的一方，使用较小的减去当前值即可
    https://leetcode-cn.com/problems/trapping-rain-water/solution/dong-tai-gui-hua-shuang-zhi-zhen-tu-jie-by-ml-zimi/
    """
    if not height:
        return 0
    left = 0
    right = len(height)-1
    leftmax = height[0]
    rightmax = height[-1]
    total = 0
    while left<right:
        leftmax = max(height[left], leftmax)
        rightmax = max(height[right], rightmax)
        if leftmax<rightmax:
            total += leftmax-height[left]
            left+=1
        else:
            total += rightmax-height[right]
            right-=1
    return total

print trap([0,1,0,2,1,0,1,3,2,1,2,1])


"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
说明：你不能倾斜容器，且 n 的值至少为 2。
<img>https://aliyun-lc-upload.oss-cn-hangzhou.aliyuncs.com/aliyun-lc-upload/uploads/2018/07/25/question_11.jpg</img>

示例：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
"""
def maxArea(height):
    """
    双指针，分别从左到右，从右到左
    选取当前左右高度最小的一个与水平距离相乘
    乘积与已知最大面积做比较
    :param height:
    :return:
    """
    count = len(height)
    left = 0
    right = count-1
    maxsum = 0
    while left<right:
        tmpheight = min(height[left], height[right])
        tmparea = tmpheight*(right-left)
        if tmparea>maxsum:
            maxsum = tmparea
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return maxsum
print maxArea([1,8,6,2,5,4,8,3,7])
"""
"""



