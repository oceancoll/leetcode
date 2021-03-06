# 旋转矩阵
给你一幅由 N × N 矩阵表示的图像，其中每个像素的大小为 4 字节。  
请你设计一种算法，将图像旋转 90 度。  
不占用额外内存空间能否做到？

---
示例 1:  
```text
给定
matrix = 
    [
      [1,2,3],
      [4,5,6],
      [7,8,9]
    ],
```

```text
原地旋转输入矩阵，使其变为:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
```  

---
示例 2:  
```text
给定 
matrix =
    [
      [ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]
    ], 
```
```text
原地旋转输入矩阵，使其变为:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
```

---
思路：

先将原数组，以行数的中间值进行对折，如果行数为奇数，则中间行为对折线。如果行数为偶数，则中间的空白线为对折线  

```text
原始数组
 5  1  9 11
 2  4  8 10
13  3  6  7
15 14 12 16


水平翻转
 5  1  9 11                 15 14 12 16
 2  4  8 10                 13  3  6  7
------------   =水平翻转=>   ------------
13  3  6  7                  2  4  8 10
15 14 12 16                  5  1  9 11


再根据主对角线 \backslash\ 翻转得到：
15 14 12 16                   15 13  2  5
13  3  6  7   =主对角线翻转=>   14  3  4  1
 2  4  8 10                   12  6  8  9
 5  1  9 11                   16  7 10 11
```


[leetcode地址](https://leetcode-cn.com/problems/rotate-matrix-lcci/)
