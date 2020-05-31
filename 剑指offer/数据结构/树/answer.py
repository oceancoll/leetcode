# coding:utf-8
class Node(object):
    # 节点结构
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    # 树结构
    def __init__(self):
        self.root = None
        self.count = 0
        self.max_sum = float('-inf')
        self.max_num = 0

    def add(self, data):
        # 添加子节点
        node = Node(data)
        if not self.root:
            # 为空树直接赋值
            self.root = node
        else:
            # 遍历树，左节点不存在，赋值给左节点。右节点不存在，赋值给右节点
            # 均存在时，继续向下搜索
            queue = [self.root]
            while queue:
                currnode = queue.pop(0)
                if not currnode.left:
                    currnode.left = node
                    return
                elif not currnode.right:
                    currnode.right = node
                    return
                else:
                    queue.append(currnode.left)
                    queue.append(currnode.right)
    def bfs(self, root):
        # 广度优先
        # 根据先入先出的原则。先检查左节点，再检查右节点
        # 二叉树的左右视图，是bfs层级遍历时，如果是左视图，则取每行的最左侧节点，如果是右视图取每行最右侧节点
        if not root:
            return
        queue = [root]
        value = []
        while queue:
            currnode = queue.pop(0)
            value.append(currnode.data)
            if currnode.left:
                queue.append(currnode.left)
            if currnode.right:
                queue.append(currnode.right)
        return value

    def bfs2(self, root):
        # 广度优先(位于同一层的数据在一行返回)
        # 主行遍历加入返回
        if not root:
            return
        resultList = []
        curLayer = [root]  # 当前行
        while curLayer:
            curList = []  # 当前行的结果
            nextLayer = []  # 下一行
            for node in curLayer:
                curList.append(node.data)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            resultList.append(curList)  # 该行结果加入最后结果
            curLayer = nextLayer  # 下一行替换当前行
        return resultList

    def bfs3(self, root):
        # 广度优先 之字型 返回(位于同一层的数据在一行返回，偶数行倒序返回)
        if not root:
            return
        resultList = []
        curLayer = [root]
        isEvenLayer = True  # 是否偶数行标志
        while curLayer:
            curList = []
            nextLayer = []
            for node in curLayer:
                curList.append(node.data)
                if node.left:
                    nextLayer.append(node.left)
                if node.right:
                    nextLayer.append(node.right)
            isEvenLayer = not isEvenLayer  # 取反 来判断是否偶数行
            resultList.append(curList[::-1] if isEvenLayer else curList)
            curLayer = nextLayer
        return resultList

    def dfs(self, root):
        # 深度优先遍历(递归法)
        if not root:
            return
        print root.data
        self.dfs(root.left)
        self.dfs(root.right)

    def dfs1(self, root):
        # 深度优先遍历(非递归法)
        # 根据先入后出的原则。先检查右节点，再检查左节点
        if not root:
            return
        queue = [root]
        value = []
        while queue:
            currnode = queue.pop()
            value.append(currnode.data)
            if currnode.right:
                queue.append(currnode.right)
            if currnode.left:
                queue.append(currnode.left)
        return value

    def preorder(self, root):
        # 前序遍历
        # 根-左-右
        if not root:
            return
        print root.data
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self, root):
        # 中序遍历
        # 左-根-右
        if not root:
            return
        self.preorder(root.left)
        print root.data
        self.preorder(root.right)

    def backorder(self, root):
        # 后序遍历
        # 左-右-根
        if not root:
            return
        self.preorder(root.left)
        self.preorder(root.right)
        print root.data

    def kthnode(self, root, k):
        # 搜索二叉树第k个节点，搜索二叉树为中序排列有序的二叉树。故中叙遍历的第k个点即为所求值
        # https://blog.csdn.net/u010005281/article/details/79788675
        if not root:
            return
        node = self.kthnode(root.left, k)
        if node:
            return node
        self.count +=1
        if self.count == k:
            return root
        node = self.kthnode(root.right, k)
        if node:
            return node

    def maxdepth(self, root):
        if not root:
            return 0
        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)
        return max(left, right) + 1

    def mirror(self, root):
        # 二叉树的镜像
        # 左右交换，递归镜像
        if not root:
            return
        root.left, root.right = root.right, root.left
        self.mirror(root.left)
        self.mirror(root.right)
        return root

    def isbalance(self, root):
        # 是否平衡树
        # 平衡树条件：空树 或者 左右树高度差不超过1且左右树均为平衡树
        if not root:
            return True
        return abs(self.maxdepth(root.left)-self.maxdepth(root.right))<=1 and self.isbalance(root.left) and self.isbalance(root.right)

    def isSymmetrical(self, root):
        # 是否对称二叉树
        # 左右节点都没有值，则是
        # 一个节点有，一个节点没有，则不是
        # 有节点值不同，则不是
        # 递归对左右进行判断
        def is_mirror(left, right):
            if not left and not right:
                return True
            elif not left or not right:
                return False
            if left.data != right.data:
                return False
            ret1 = is_mirror(left.left, right.right)
            ret2 = is_mirror(left.right, right.left)
            return ret1 and ret2
        if not root:
            return True
        return is_mirror(root.left, root.right)

    def VerifySquenceOfBST(self, sequence):
        # https://blog.csdn.net/u010005281/article/details/79401276
        # 判断一个列表是否为某搜索二叉树的后序排序
        # 搜素二叉树的左子树的值均小于根节点，右子树的值均大于根节点
        # 后序排序的最后一个值为根节点的值
        # 先根据上述条件，将数组分为两部分，判断是否满足条件
        # 对于满足条件时，再递归查询左子树和右子树
        if not sequence:
            return False
        root = sequence[-1]
        mid = 0
        for i in range(len(sequence)):
            mid = i
            if sequence[i]>root:
                break
        if mid < len(sequence)-1:
            for i in sequence[mid:-1]:
                if i < root:
                    return False
        left_flag = True
        right_flag = True
        if mid > 0:
            left_flag = self.VerifySquenceOfBST(sequence[:mid])
        if mid < len(sequence)-1:
            right_flag = self.VerifySquenceOfBST(sequence[mid:len(sequence)-1])
        return left_flag and right_flag

    def HasSubtree(self, pRoot1, pRoot2):
        # https://blog.csdn.net/u010005281/article/details/79460325
        # 两棵二叉树AB，判断B是不是A的子结构
        # 定位ab的交点，再判断b是不是A的子结构
        if not pRoot1 or not pRoot2:
            return False
        result = False
        if pRoot1.data == pRoot2.data:
            result = self.isSubtree(pRoot1, pRoot2)
        if result == False:
            result = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return result

    def isSubtree(self,root1,root2):
        # 有相同节点时，判断其余节点是否相同
        if not root2:
            return True
        if not root1:
            return False
        if root1.data == root2.data:
            return self.isSubtree(root1.left, root2.left) and self.isbalance(root1.right, root2.right)
        return False

    def maxPathSum(self, root):
        # 给定一个非空二叉树，返回最大路径和
        # https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
        # 本题中，路径被定义为一条从树中任意节点出发，达到任意节点的序列。该路径至少包含一个节点，且不一定经过根节点
        # https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/solution/er-cha-shu-de-zui-da-lu-jing-he-by-leetcode/
        """
            示例 1:
                输入: [1,2,3]
                       1
                      / \
                     2   3
            输出: 6
            示例 2:
                输入: [-10,9,20,null,null,15,7]
                       -10
                       / \
                      9  20
                        /  \
                       15   7
            输出: 42
        """
        def max_gain(node):
            # 获取最大路径值
            if not node:
                return 0
            # 获取左侧最大值
            left_gain = max(max_gain(node.left),0)
            # 获取右侧最大值
            right_gain = max(max_gain(node.right),0)
            # 对左右中取最大和
            newpath = node.data + left_gain + right_gain
            # 获取最大值
            self.max_sum = max(self.max_sum, newpath)
            # 返回最大的路径
            return node.data + max(left_gain, right_gain)
        max_gain(root)
        return self.max_sum

    def longestUnivaluePath(self, root):
        # 最长同值路径
        # 给定一个二叉树，找到最长的路径，这个路径中的每个节点具有相同值。 这条路径可以经过也可以不经过根节点。
        # https://leetcode-cn.com/problems/longest-univalue-path/solution/zui-chang-tong-zhi-lu-jing-by-leetcode/
        """
            示例 1:
                输入:
                      5
                     / \
                    4   5
                   / \   \
                  1   1   5
                输出:
                2

            示例 2:
                输入:
                      1
                     / \
                    4   5
                   / \   \
                  4   4   5
                输出:
                2
        """
        def arrow_length(node):
            if not node:
                return 0
            # 获取左侧已计算长度
            left_len = arrow_length(node.left)
            # 获取右侧已计算长度
            right_len = arrow_length(node.right)
            # 左临时长度
            left_arrow = 0
            # 右临时长度
            right_arrow = 0
            # 左侧有相同节点
            if node.left and node.left.data == node.data:
                left_arrow = left_len+1
            # 右侧有相同节点
            if node.right and node.right.data == node.data:
                right_arrow = right_len+1
            # 计算最大长度
            self.max_num = max(self.max_num, left_arrow+right_arrow)
            # 返回最大路径值
            return max(left_arrow, right_arrow)

        arrow_length(root)
        return self.max_num


    def diameterOfBinaryTree(self, root):
        # 找到树中距离最大的两个结点
        # 两种情况
        # 1. 如果最远的两个节点经过了根节点，那么最远的距离就是，左侧最大深度加上右侧最大深度
        # 2. 如果最远的两个根节点不经过根节点(只有1侧树的情况),最大距离是一个子树上的两个叶子节点的距离
        if not root:
            return 0
        # 只有左侧时的最大距离
        max_tmp_left = self.diameterOfBinaryTree(root.left)
        # 只有右侧时的最大距离
        max_tmp_right = self.diameterOfBinaryTree(root.right)
        # 对比经过根节点的距离(两侧最大高度和) 与 单侧的最大距离
        max_legth = max(self.maxdepth(root.left)+self.maxdepth(root.right), max_tmp_left, max_tmp_right)
        return max_legth

    def lowestCommonAncestor(self, root, p, q):
        # 二叉树的最近公共祖先
        # root: 树 p:节点a  q：节点b
        # https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/solution/236-er-cha-shu-de-zui-jin-gong-gong-zu-xian-hou-xu/
        # 当树不存在或者与任意一个节点相同
        if not root or root ==p or root==q:
            return root
        # 左树找两个节点
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p,q)
        if not left:
            return right
        if not right:
            return left
        return root






def rebuildtree(preorder, inorder):
    """
    重建二叉树
    根据前序遍历和中序遍历，还原二叉树
    前序遍历的第一个节点为根节点
    中序遍历根节点左侧的数据长度等于前序遍历的左侧长度
    :param preorder: 前序遍历
    :param inorder: 中序遍历
    :return:
    """
    if not preorder or not inorder:
        return
    root = Node(preorder[0])  # 根节点
    mid = inorder.index(preorder[0])  # 根节点位于中序遍历的位置
    # 递归左右树，去除掉根节点
    root.left = rebuildtree(preorder[1:mid+1], inorder[:mid])
    root.right = rebuildtree(preorder[mid+1:], inorder[mid+1:])
    return root


# 根据前序遍历，中序遍历，重建二叉树
atree = rebuildtree([1, 2, 4, 7, 3, 5, 6, 8], [4, 7, 2, 1, 5, 3, 8, 6])
tree = Tree()
# 广度优先遍历
print tree.bfs(atree)
# 广度优先遍历(位于同一层的数据在一行返回)
print tree.bfs2(atree)
# 广度优先 之字型 返回(位于同一层的数据在一行返回，偶数行倒序返回)
print tree.bfs3(atree)
# 深度优先遍历(递归法)
print tree.dfs(atree)
# 深度优先遍历(非递归法)
print tree.dfs1(atree)
# 前序遍历
print tree.preorder(atree)
# 中序遍历
print tree.inorder(atree)
# 后序遍历
print tree.backorder(atree)
# 搜索二叉树第k个节点
print tree.kthnode(atree, 3)
# 最大树深
print tree.maxdepth(atree)
# 二叉树镜像
mirror_tree = tree.mirror(atree)
print tree.bfs(mirror_tree)
