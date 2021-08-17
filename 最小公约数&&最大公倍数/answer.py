# coding:utf-8
"""
使用辗转相除法计算最大公约数
最小公倍数=m*n/最大公约数
"""
def getMaxcommpisor(m,n):
    if m<n:
        m,n = n,m  # 保证m>n
    while m%n!=0:
        m,n = n, m%n
    return n
print getMaxcommpisor(8,4)