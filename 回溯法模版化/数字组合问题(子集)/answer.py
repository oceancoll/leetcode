# coding:utf-8

"""
找出从自然数1、2、3、...、n中任取r个数的所有组合。
例如，n=5，r=3的所有组合为：
1,2,3
1,2,4
1,2,5
1,3,4
1,3,5
1,4,5
2,3,4
2,3,5
2,4,5
3,4,5
"""

n = 5
r = 3
a = [1,2,3,4,5]

# 一个解
x = [0] * n
# 一组解
X = []

# 剪枝函数
def conflict(k):
    global x, r, n
    # 当前k个值满足的已经超过r，或者，前k个满足的个数，加上后面剩余的个数，超过r.这些个条件下均不满足要求
    if sum(x[:k+1]) > r or (sum(x[:k+1]) + n-k-1) < r:
        return True
    return False

# 入口
def comb(k):
    global x, X
    # 边界值
    if k>=n:
        X.append(x[:])
    else:
        # 对于解的长度固定的情况，使用[1,0]解，x[k]=1的方式
        for i in [1,0]:
            x[k] = i
            # 剪枝函数
            if not conflict(k):
                # 检测下一个点
                comb(k+1)

# 根据一个解，获得具体代表的数字
def get_a_comb(x):
    global a
    return [a[m] for m,n in enumerate(x) if n == 1]

# 获取所有解代表的数字
def get_all_comb(X):
    global a
    result = []
    for x in X:
        result.append([a[m] for m,n in enumerate(x) if n == 1])
    return result

comb(0)
print X[0]
print get_a_comb(X[0])
print get_all_comb(X)