# coding:utf-8
"""
一个字符串中，只包含'(',')','{','}','['和']',判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

输入："[" 输出：false
输入："[]" 输出：true

思路：
    维护一个map,用来存关闭括号与开始括号的映射关系
    遇到开始括号入栈，遇到关闭括号，判断栈的最后一个字符是否与该该关闭括号为映射关系
    最后通过判断栈中是否还有元素，以及flag来判断
"""


def isValid(s):
    m = {")": "(", "}": "{", "]": "["}
    stack = []
    flag = True
    for i in s:
        if i in m:
            if stack and stack[-1] == m.get(i):
                stack.pop()
            else:
                flag = False
                break
        else:
            stack.append(i)
    return flag and not stack

print isValid("[]")
