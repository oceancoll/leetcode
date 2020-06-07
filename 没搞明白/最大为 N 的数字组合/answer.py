# coding:utf-8
"""
我们有一组排序的数字 D，它是  {'1','2','3','4','5','6','7','8','9'} 的非空子集。（请注意，'0' 不包括在内。）

现在，我们用这些数字进行组合写数字，想用多少次就用多少次。例如 D = {'1','3','5'}，我们可以写出像 '13', '551', '1351315' 这样的数字。

返回可以用 D 中的数字写出的小于或等于 N 的正整数的数目。

 

示例 1：

输入：D = ["1","3","5","7"], N = 100
输出：20
解释：
可写出的 20 个数字是：
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
https://leetcode-cn.com/problems/numbers-at-most-n-given-digit-set/solution/python3shi-jian-kong-jian-on-by-gorilla/
"""


class Solution:
    def atMostNGivenDigitSet(self, D, N):
        logits = str(N + 1)
        m = len(logits)
        ans = 0
        f = [1]  # f[i]=len(D)**i

        for i in range(1, m):  # 长度小于m
            f.append(f[-1] * len(D))
            ans += f[-1]

        for i in range(m):  # 长度等于m
            count = 0
            for d in D:  # 如果将第i位设为一个比logits[i]更小的数，那么后面m-i-1位可以随意
                if d < logits[i]:
                    count += 1
                else:
                    break
            ans += f[m - i - 1] * count
            # 如果D中没有与logits[i]相等的数，结束循环，否则下一次循环时的前缀是logits[0, i]
            if count == len(D) or count < len(D) and D[count] > logits[i]:
                break
        return ans
