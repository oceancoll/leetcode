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

    def removeNthFromEnd(self, head, n):
        """
        删除链表倒数第n个节点
        思路：使用临时节点的方式与快慢指针
        因为n恰好在n节点上，故需要向上取一位
        """
        sentinal = Node(0)
        sentinal.next = head
        slow, fast = sentinal, head
        for i in range(n):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return sentinal.next



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

    def swapPairs(self):
        # 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
        # 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
        # 示例:
        # 给定 1->2->3->4, 你应该返回 2->1->4->3.
        # https://leetcode-cn.com/problems/swap-nodes-in-pairs/solution/xian-jian-san-ge-yin-yong-zhi-xiang-san-ge-jie-dia/

        # 新建2个引用指向一个节点，并将这个节点的next指向head，用以记录初始节点
        head = self.head
        sentinal = Node(0)
        sentinal.next = head
        pre = sentinal
        while pre.next and pre.next.next:
            # 分别拿3个引用指向这三个节点
            node1 = pre.next
            node2 = pre.next.next
            pre.next = node2
            node1.next = node2.next
            node2.next = node1
            pre = node1
        # 最后返回初始节点
        return sentinal.next

    def reverseKGroup(self, head, k):
        """
        给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
        输入：head = [1,2,3,4,5], k = 3
        输出：[3,2,1,4,5]
        不足的保持原状即可

        用栈，我们把 k 个数压入栈中，然后弹出来的顺序就是翻转的！
        这里要注意几个问题：
            第一，剩下的链表个数够不够 k 个（因为不够 k 个不用翻转）；
            第二，已经翻转的部分要与剩下链表连接起来。
        """
        sentinal = Node(0)
        pre = sentinal
        while True:
            count = k
            tmp = head
            stack = []
            # k个节点入栈
            while count and tmp:
                stack.append(tmp)
                tmp = tmp.next
                count-=1
            # 如果不足k个则不用反转
            if count:
                pre.next = head
                break
            # 弹出顺序已经反向
            while stack:
                pre.next = stack.pop()
                pre = pre.next
            # 与剩下的部分连接起来
            pre.next = tmp
            # 重新赋值剩余部分
            head = tmp
        return sentinal.next

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
            head = head.next
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
        while head and head.next:
            if head.data == head.next.data:
                val = head.data
                curr = head
                while curr and curr.data == val:
                    curr = curr.next
                head.next = curr
            head = head.next

    def deleteDuplicatesii(self, head):
        # 删除排序链表中的连续重复元素(连续重复值则均不保留)
        # 链表1->2->3->3->4->4->5 处理后为 1->2->5
        # 使用双指针，与哨兵节点
        # 当head节点当前值与head下一个节点值相同时，则不断向后搜索是否与第一个值相同。当不同时，则把哨兵节点的下一个值指向head节点
        # 当head节点当前值与head下一个节点值不同时，则哨兵节点指向head节点，head节点向后搜索
        # 最后输出哨兵节点(去除掉临时节点)
        # https://blog.csdn.net/u010005281/article/details/80232730
        sentinal = Node(0)
        sentinal.next = head
        pre, curr = sentinal, head
        while curr and curr.next:
            if curr.data == curr.next.data:
                val = curr.data
                while curr and curr.data == val:
                    curr = curr.next
                pre.next = curr
            else:
                pre = curr
                curr = curr.next
        return sentinal.next

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

    def addTwoNumbers2(self, l1, l2):
        # 链表求和
        # 使用哨兵节点
        """
        https://www.nowcoder.com/practice/c56f6c70fb3f4849bc56e33ff2a50b6b
        给定两个用链表表示的整数，每个节点包含一个数位。
        正向求和，也就是937+63=1000
        编写函数对这两个整数求和，并用链表形式返回结果。
        示例：
            链表 1 为 9->3->7，链表 2 为 6->3，
            最后生成新的结果链表为 1->0->0->0。
        思路：和反向求和相同，只是在求和前和求和后，进行反转链表即可
        """
        # 临时数字和
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
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
        return self.reverseList(sentinal.next)

    def sortInList(self, head):
        """
        给定一个无序单链表，实现单链表的排序(按升序排序)
        输入：[1,3,2,4,5]
        返回值：{1,2,3,4,5}
        思路：
        通过快慢指针的方式，将链表分为2部分，然后使用归并排序的方式，进行排序
        """
        def merge(left, right):
            sentinal = Node(0)
            pre = sentinal
            while left and right:
                if left:
                    pre.next = left
                    pre = pre.next
                    left = left.next
                else:
                    pre.next = right
                    pre = pre.next
                    right = right.next
            if left:
                pre.next = left
            if right:
                pre.next = right
            return sentinal.next

        if not head or not head.next:
            return head
        slow = head
        fast = head
        while fast.next and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        left = self.sortInList(head)
        right = self.sortInList(mid)
        return merge(left, right)

    def reverseBetween(self, head, m, n):
        """
        链表指定区域的反转
        https://leetcode-cn.com/problems/reverse-linked-list-ii/solution/fan-zhuan-lian-biao-ii-by-leetcode-solut-teyq/
        pre:为待反转节点的前一个节点
        curr:待反转节点的第一个节点
        next:curr的下一个节点
        步骤1：找到curr的下一个节点
        步骤2：将curr的next指向next.next
        步骤3：将next的下一个指向pre的下一个
        步骤4：将pre的下一个指向next节点
        最后返回虚拟节点的next
        """
        sentinal = Node(0)
        sentinal.next = head
        pre = sentinal
        for _ in range(m-1):
            pre = pre.next
        curr = pre.next
        for _ in range(n-m):
            next = curr.next
            curr.next = next.next
            next.next = pre.next
            pre.next = next
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

