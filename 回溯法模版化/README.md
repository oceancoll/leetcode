# 回溯法模板化
### 1.定义
- 也叫试探法，它是一种系统地搜索问题的解的方法。
### 2.基本思想
- 从一条路往前走，能进则进，不能进则退回来，换一条路再试。
### 3.一般步骤
- 定义一个解空间（子集树、排列树二选一），针对于不同问题
- 利用适于搜索的方法组织解空间
- 利用深度优先法搜索解空间
- 利用剪枝函数避免移动到不可能产生解的子空间
### 4.约束函数
- 是否满足显约束（存在）,边界值
### 5.限界函数
- 是否满足隐约束（最优）
### 6.子集树模板
```text
·顾名思义：单条结果是候选值的子集
```
- 遍历子集树，时间复杂度 O(2^n)
- 如果解的长度是不固定的，那么解和元素顺序无关，即可以从中选择0个或多个。例如：子集，迷宫，...
- 如果解的长度是固定的，那么解和元素顺序有关，即每个元素有一个对应的状态。例如：子集，8皇后，...
- 解空间的个数指数级别的，为2^n,可以用子集树来表示所有的解，适用于：幂集、子集和、0-1背包、装载、8皇后、迷宫、...

    ***a.子集树模板递归版***
```python
n = 4             # 最大边界值
a = [1, 2, 3, 4]  # 候选集
x = []            # 一个解（n元0-1数组）
X = []            # 一组解

# 冲突检测：无
def conflict(k):
    global n, x, X, a
    
    return False # 无冲突
    
# 一个例子
# 冲突检测：八皇后问题
def conflict2(k):
    global n, x, X, a
    
    if k==0:
        return False
    
    # 根据部分解，构造部分集
    s = [y[0] for y in filter(lambda s:s[1]!=0, zip(a[:k+1],x[:k+1]))]
    if len(s)==0:
        return False
    if 0 < sum(map(lambda y:y%2, s)) < len(s) or sum(s) >= 8: # 只比较 x[k] 与 x[k-1] 奇偶是否相间
        return True
    
    return False # 无冲突

# 子集树递归模板
def subsets(k): # 到达第k个元素
    global n, x, X
    
    if k >= n:  # 超出最尾的元素
        #print(x)
        X.append(x[:]) # 保存（一个解）
    else:
        for i in [1, 0]: # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            """若解的长度不固定"""
            x.append(i)
            if not conflict2(k): # 剪枝
                subsets(k+1)
            x.pop()              # 回溯
            """若解的长度固定，固定是指[]中的值长度固定，只是会有0，1变化
            for i in [1, 0]: # 遍历元素 a[k] 的两种选择状态:1-选择，0-不选
            x[k] = i
            if not conflict(k): # 剪枝
                comb(k+1)
            """



# 根据一个解x，构造一个子集
def get_a_subset(x):
    global a
    
    return [y[0] for y in filter(lambda s:s[1]!=0, zip(a,x))]

# 根据一组解X, 构造一组子集
def get_all_subset(X):
    return [get_a_subset(x) for x in X]

# 测试
subsets(0)

# 查看第3个解，及对应的子集
#print(X[2])
#print(get_a_subset(X[2]))

print(get_all_subset(X))
```
### 7.排列树模板
```text
·顾名思义：由n个元素排列而成
```
- 遍历排列树，时间复杂度O(n!)
- 解空间是由n个元素的排列形成，也就是说n个元素的每一个排列都是解空间中的一个元素，那么，最后解空间的组织形式是排列树
- 适用于：n个元素全排列、旅行商、...

    ***a.排列树模板递归版***
```python
"""求[1,2,3,4]的全排列"""
n = 4
x = [1,2,3,4] # 一个解
X = []        # 一组解


# 冲突检测：无
def conflict(k):
    global n, x, X
    
    return False # 无冲突


# 一个例子
# 冲突检测：元素奇偶相间的排列
def conflict2(k):
    global n, x, X
    
    if k==0:                   # 第一个元素，肯定无冲突
        return False
        
    if x[k-1] % 2 == x[k] % 2: # 只比较 x[k] 与 x[k-1] 奇偶是否相同
        return True
        
    return False # 无冲突
    

# 排列树递归模板
def backkrak(k): # 到达第k个位置
    global n, x, X
    
    if k >= n:  # 超出最尾的位置
        print(x)
        #X.append(x[:]) # 注意x[:]
    else:
        for i in range(k, n): # 遍历后面第 k~n-1 的位置
            x[k], x[i] = x[i], x[k]
            if not conflict2(k):    # 剪枝
                backkrak(k+1)
            x[i], x[k] = x[k], x[i] # 回溯
            
# 测试
backkrak(0)
```