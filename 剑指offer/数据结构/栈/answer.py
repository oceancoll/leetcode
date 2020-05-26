# coding:utf-8

def validateStackSequences(pushed, popped):
    """
    验证栈序列
    给定 pushed 和 popped 两个序列，每个序列中的 值都不重复，
    只有当它们可能是在最初空栈上进行的推入 push 和弹出 pop 操作序列的结果时，
    返回 true；否则，返回 false

    输入：pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
    输出：true
    解释：我们可以按以下顺序执行：
    push(1), push(2), push(3), push(4), pop() -> 4,
    push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
    :param self:
    :param pushed:
    :param popped:
    :return:
    """
    stack = []
    index = 0
    # 通过建立一个list,对pushed的值进行逐一排查，通过index来控制popped

    while pushed:
        stack.append(pushed.pop(0))
        while stack and stack[-1] == popped[index]:
            stack.pop()
            index+=1
    return not stack

pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]
print validateStackSequences(pushed, popped)