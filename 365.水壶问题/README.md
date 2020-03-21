# 365. 水壶问题
有两个容量分别为 x升 和 y升 的水壶以及无限多的水。  
请判断能否通过使用这两个水壶，从而可以得到恰好 z升 的水？ 
如果可以，最后请用以上水壶中的一或两个来盛放取得的 z升 水。

你允许：

装满任意一个水壶  
清空任意一个水壶  
从一个水壶向另外一个水壶倒水，直到装满或者倒空  
示例 1: (From the famous "Die Hard" example)

输入: x = 3, y = 5, z = 4  
输出: True  
示例 2:  

输入: x = 2, y = 6, z = 5  
输出: False

[leetcode地址](https://leetcode-cn.com/problems/water-and-jug-problem/)

---

- 解题策略

我们可以认为每次操作只会给水的总量带来 x 或者 y 的变化量。  
因此我们的目标可以改写成：找到一对整数 a,b，使得  
&nbsp;&nbsp;&nbsp;&nbsp;ax+by=z  
&nbsp;&nbsp;&nbsp;&nbsp;ax+by=z

而只要满足 z≤x+y，且这样的 a,b 存在，那么我们的目标就是可以达成的。  
这是因为：  
&nbsp;&nbsp;&nbsp;&nbsp;若a≥0,b≥0，那么显然可以达成目标。  
&nbsp;&nbsp;&nbsp;&nbsp;若 a<0，那么可以进行以下操作：  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;往 y 壶倒水；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;把 y 壶的水倒入 x 壶；

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果 y 壶不为空，那么 x 壶肯定是满的，把 x 壶倒空，然后再把 y 壶的水倒入 x 壶。

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;重复以上操作直至某一步时 x 壶进行了 aa 次倒空操作，y 壶进行了 bb 次倒水操作。

&nbsp;&nbsp;&nbsp;&nbsp;若 b<0，方法同上，x 与 y 互换。

而贝祖定理告诉我们，ax+by=z 有解当且仅当 z 是 x,y 的最大公约数的倍数。  
因此我们只需要找到 x,y 的最大公约数并判断 z 是否是它的倍数即可