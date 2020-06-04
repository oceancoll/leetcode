# coding:utf-8
class Node(object):
    # 链表节点
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkList(object):
    def __init__(self):
        self.head = None

    def length(self):
        # 链表长度
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def items(self):
        # 遍历链表的数据
        result = []
        cur = self.head
        while cur:
            result.append(cur.data)
            cur = cur.next
        return result

    def add(self, data):
        # 向头添加数据
        node = Node(data)
        node.next = self.head
        self.head = node

    def append(self, data):
        # 向尾增加数据
        node = Node(data)
        if not self.head:
            # 链表为空时，直接插入
            self.head = node
        else:
            # 链表不为空时
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node

    def insert(self, k, data):
        # 向指定位置k插入data
        # 当节点小于等于0时，向头部插入
        if k<=0:
            self.add(data)
        # 当节点大于等于最后一位时，向尾部插入
        elif k>=self.length()-1:
            self.append(data)
        else:
            node = Node(data)
            count = 1
            cur = self.head
            while cur and count !=k:
                cur = cur.next
            node.next = cur.next
            cur.next = node
            self.head = cur

    def find(self, data):
        # 查找data是否在链表中
        return data in self.items()

    def get_value(self, index):
        # 根据指定索引位置获取数据
        if 0<=index<=self.length()-1:
            count = 0
            cur = self.head
            while cur and count!=index:
                count+=1
                cur = cur.next
            return cur.data

    def remove_index(self, index):
        # 删除指定位置的元素
        if index>=0 and index<=self.length()-1:
            if index==0:
                cur = self.head
                self.head = cur.next
            else:
                cur = self.head
                count = 1
                while cur and count !=index:
                    count+=1
                    cur = cur.next
                cur.next = cur.next.next

    def remove_value(self, data):
        # 删除指定元素
        # 使用哨兵节点
        # https://leetcode-cn.com/problems/remove-linked-list-elements/solution/yi-chu-lian-biao-yuan-su-by-leetcode/
        head = self.head
        sentinal = Node(0)
        sentinal.next = head
        pre, curr = sentinal, head
        while curr:
            if curr.data == data:
                pre.next = curr.next
            else:
                pre = curr
            curr = curr.next
        return sentinal.next

    def clear(self):
        self.head = None

    def print_reverse_linklist(self):
        # 从尾到头打印链表
        cur = self.head
        list1 = []
        while cur:
            list1.append(cur.data)
            cur = cur.next
        return list1[::-1]

    def FindKthToTail(self, k):
        # 链表倒数第k个节点
        # 使用快慢指针
        # https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/solution/yi-chong-jian-dan-jie-fa-by-ai-bian-cheng-de-zhou-/
        fast = self.head
        slow = self.head
        for i in range(k):
            # 校验边界值
            if fast:
                fast = fast.next
            else:
                return None
        while fast:
            fast = fast.next
            slow = slow.next
        return slow

    def reverseList(self):
        # 反转链表，生成新的链表
        # 使用双指针迭代
        # https://leetcode-cn.com/problems/reverse-linked-list/solution/dong-hua-yan-shi-206-fan-zhuan-lian-biao-by-user74/
        head = self.head
        prenode = None
        while head:
            nextnode = head.next
            head.next = prenode
            head, prenode = nextnode, head
        return prenode

    def mergeTwoLists(self, l1, l2):
        # 合并两个有序链表
        # 将两个升序链表合并为一个新的升序链表并返回。
        # 新链表是通过拼接给定的两个链表的所有节点组成的
        # https://leetcode-cn.com/problems/merge-two-sorted-lists/solution/he-bing-liang-ge-you-xu-lian-biao-by-leetcode-solu/
        # 使用递归
        if not l1:
            return l2
        elif not l2:
            return l1
        elif l1.data < l2.data:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeKLists(self, lists):
        # 合并K个有序链表
        # https://leetcode-cn.com/problems/merge-k-sorted-lists/solution/leetcode-23-he-bing-kge-pai-xu-lian-biao-by-powcai/
        # 通过分而治之的思想，将链表两两合并
        if not lists:
            return
        count = len(lists)
        return self.merge(lists, 0, count-1)

    def merge(self, lists, left, right):
        if left == right:
            return lists[left]
        mid = (left + right) / 2
        l1 = self.merge(lists, left, mid)
        l2 = self.merge(lists, mid+1, right)
        return self.mergeTwoLists(l1, l2)

    def split_list(self, head):
        """
        根据奇偶位置将链表拆分为2个链表
        https://www.cnblogs.com/terry-c/p/9866083.html
        :param head:
        :return:
        """
        jihead = ouhead = None
        jicur = oucur = None
        count = 0
        while head:
            if count % 2 ==1:
                if not jicur:
                    jihead = jicur = head
                else:
                    jicur.next = head
                    jicur = jicur.next
            else:
                if not oucur:
                    ouhead = oucur = head
                else:
                    oucur.next = head
                    oucur = oucur.next
            count+=1
        # 因为是直接赋值链表位置，故带有下一位，因此将后面的全置为None
        jicur.next = None
        oucur.next = None
        return jihead, ouhead

    def getIntersectionNode(self, headA, headB):
        # 找到两个单链表相交的起始节点
        # 使用hash表
        # https://leetcode-cn.com/problems/intersection-of-two-linked-lists/solution/zhong-gui-zhong-ju-de-ha-xi-suan-fa-by-tuotuoli/
        s1 = set()
        while headA:
            s1.add(headA)
            headA = headA.next
        while headB:
            if headB in s1:
                return headB
            headB = headB.next
        return None

    def deleteDuplicates(self, head):
        # 删除排序链表中的连续重复元素(保留第一个重复值)
        # 链表1->2->3->3->4->4->5 处理后为 1->2->3->4->5
        # 使用双指针，当快指针的值和慢指针相同时，不做操作
        # 当不同时，慢指针向前移动一位，同时快指针的值赋给慢指针
        # 快指针到头后，将慢指针指向空
        # https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/solution/dong-hua-yan-shi-83-shan-chu-pai-xu-lian-biao-zhon/
        if not (head and head.next):
            return head
        i, j = head, head
        while j:
            if i.data != j.data:
                i = i.next
                i.data = j.data
            j = j.next
        i.next = None
        return head

    def deleteDuplicatesii(self, head):
        # 删除排序链表中的连续重复元素(连续重复值则均不保留)
        # 链表1->2->3->3->4->4->5 处理后为 1->2->5
        # 使用双指针，与哨兵节点
        # 当head节点当前值与head下一个节点值相同时，则不断向后搜索是否与第一个值相同。当不同时，则把哨兵节点的下一个值指向head节点
        # 当head节点当前值与head下一个节点值不同时，则哨兵节点指向head节点，head节点向后搜索
        # 最后输出哨兵节点(去除掉临时节点)
        # https://blog.csdn.net/u010005281/article/details/80232730
        tmpnode = Node(0)
        tmpnode.next = head
        last = tmpnode
        while head and head.next:
            if head.data == head.next.data:
                value = head.data
                while head and head.data == value:
                    head = head.next
                last.next = head
            else:
                last = head
                head = head.next
        return tmpnode.next

    def hasCycle(self, head):
        # 判断链表是否有环
        # 产生环的原因：某节点的next指向了已有的节点
        # 通过快慢指针，快指针每次走2步，慢指针每次走1步。当两者相遇时说明产生了环
        if not head:
            # 链表不存在时，不会有环
            return False
        fast, slow = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow and fast and slow.data == fast.data:
                return True
        return False

    def detectCycle(self, head):
        # 给定一个链表，返回链表入环的第一个节点
        # 使用快慢指针
        # https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/142huan-xing-lian-biao-ii-shuang-zhi-zhen-guan-f-2/
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 有环
            if slow is fast:
                # 相遇处结点meetNode
                meetnode = slow
                start = head
                # 找到入口节点
                while meetnode != start:
                    start, meetnode = start.next, meetnode.next
                return meetnode
        return None

    def addTwoNumbers(self, l1, l2):
        # 链表求和
        # 使用哨兵节点
        """
        https://leetcode-cn.com/problems/sum-lists-lcci/solution/goshuang-zhi-zhen-die-dai-ji-suan-by-kksopksjf/
        给定两个用链表表示的整数，每个节点包含一个数位。
        这些数位是反向存放的，也就是个位排在链表首部。
        编写函数对这两个整数求和，并用链表形式返回结果。
        示例：
            输入：(7 -> 1 -> 6) + (5 -> 9 -> 2)，即617 + 295
            输出：2 -> 1 -> 9，即912
        示例：
            输入：(6 -> 1 -> 7) + (2 -> 9 -> 5)，即617 + 295
            输出：9 -> 1 -> 2，即912
        """
        # 临时数字和
        tmp = 0
        # 哨兵节点
        sentinal = Node(0)
        pre = sentinal
        while l1 or l2:
            # l1 取左侧位
            if l1:
                tmp+=l1.data
                l1 = l1.next
            # l2 取左侧位
            if l2:
                tmp+=l2.data
                l2 = l2.next
            # 求当前位的数字
            pre.next = Node(tmp%10)
            # 去除最低位
            tmp = tmp/10
            pre = pre.next
        # 处理最后一位
        if tmp:
            pre.next = Node(tmp)
        return sentinal.next

# 初始化链表
link = SingleLinkList()
# 分别向尾部插入2，3，4
for i in range(3, 6):
    link.append(i)
# 向头部插入1
link.add(1)
# 向指定位置插入数据
link.insert(1, 2)
# 遍历列表数据
print link.items()
# 链表长度
print link.length()
# data是否在链表中
print link.find(3)
# 删除指定位置的数据
link.remove_index(4)
# 删除指定的值
print link.items()
# 根据指定索引位置获取数据
print link.get_value(2)
print link.items()
# 反转链表生成新链表
link.reverseList()
# 从尾到头打印链表
print link.print_reverse_linklist()
# 链表倒数第k个节点
print link.FindKthToTail(1).data
# 清空链表
link.clear()
print link.items()

