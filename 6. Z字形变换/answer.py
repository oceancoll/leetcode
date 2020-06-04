# coding:utf-8
"""
将一个给定字符串根据给定的行数，以从上往下、从左到右进行 Z 字形排列。
比如输入字符串为 "LEETCODEISHIRING" 行数为 3 时，排列如下：
    L   C   I   R
    E T O E S I I G
    E   D   H   N
之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，比如："LCIRETOESIIGEDHN"。

请你实现这个将字符串进行指定行数变换的函数：
string convert(string s, int numRows);
示例 1:
    输入: s = "LEETCODEISHIRING", numRows = 3
    输出: "LCIRETOESIIGEDHN"
示例 2:
    输入: s = "LEETCODEISHIRING", numRows = 4
    输出: "LDREOEIIECIHNTSG"
    解释:
    L     D     R
    E   O E   I I
    E C   I H   N
    T     S     G
"""

def convert(s, numRows):
    """
    根据numRows的行数，生成一个列表，按照所在行一次插入对应的行，无需真实还原出z形列表
    :param s:
    :param numRows:
    :return:
    """
    r = [[] for _ in range(numRows)]
    # 起始行
    line = 0
    # 移动方向，1:向下移动 -1:向上移动
    step = 1
    for i in s:
        # 向下时
        if step==1:
            r[line].append(i)
            line+=1
            # 掉头反向
            if line>numRows-1:
                step=-1
                line-=2
        # 向上时
        else:
            r[line].append(i)
            line-=1
            # 掉头反向
            if line<0:
                step=1
                line+=2
    return ''.join([''.join(i)for i in r])
print convert(s = "LEETCODEISHIRING", numRows = 3)