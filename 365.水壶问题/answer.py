# coding:utf-8
# 计算最大公约数
def gcd(x,y):
    # 辗转相除法
    # 通过判断两数相除的余数来判断是否能够整除
    tmp = x % y
    while tmp != 0:
        x = y
        y = tmp
        tmp = x % y
    return y

def canMeasureWater(x, y, z):
    """
    :type x: int
    :type y: int
    :type z: int
    :rtype: bool
    """
    if x == 0 or y == 0:
        return z == 0 or x + y==z
    commondata = gcd(x,y)
    return z % commondata == 0


print canMeasureWater(3,5,4)
print canMeasureWater(4,6,8)