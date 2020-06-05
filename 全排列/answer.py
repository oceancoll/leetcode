# coding:utf-8
"""
全排列
没有重复数据的情况
https://leetcode-cn.com/problems/permutations/
"""

def permute(nums):
    def dfs():
        # 跳出条件，track中的长度已经等于nums长度
        if len(track) == len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            # 该位置没有被走过
            if not used[i]:
                # 入栈
                track.append(nums[i])
                # 标记
                used[i] = True
                # 递归
                dfs()
                # 出栈
                track.pop()
                # 去除标记
                used[i] = False
    # 该位是否被查询过
    used = [False for _ in range(len(nums))]
    # 最终结果
    res = []
    # 临时结果
    track = []
    dfs()
    return res

print permute([1,2,3])

"""
全排列
有重复数据的情况
https://leetcode-cn.com/problems/permutations-ii/
"""
def permuteUnique(nums):
    def dfs():
        if len(track)==len(nums):
            res.append(track[:])
            return
        for i in range(len(nums)):
            if not used[i]:
                # 去重
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                track.append(nums[i])
                used[i] = True
                dfs()
                track.pop()
                used[i] = False
    # 排序，为了去重
    nums.sort()
    used = [False for _ in range(len(nums))]
    res = []
    track = []
    dfs()
    return res
print permuteUnique([1,2,2])