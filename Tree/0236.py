"""
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

示例 1:

输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or not p or not q:
            return None
        allNode = {}

        def saveAllNode(node: TreeNode):
            if not node:
                return
            if node.left:
                allNode[node.left.val] = node
                saveAllNode(node.left)
            if node.right:
                allNode[node.right.val] = node
                saveAllNode(node.right)

        checkp = {}
        saveAllNode(root)
        while p:
            checkp[p.val] = True
            if allNode.__contains__(p.val):
                p = allNode[p.val]
            else:
                p = None
        while q:
            if checkp.__contains__(q.val):
                return q
            if allNode.__contains__(q.val):
                q = allNode[p.val]
            else:
                q = None
        return None


"""
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
"""
root = TreeNode(val=5,
                left=TreeNode(val=4,
                              left=TreeNode(val=11,
                                            left=TreeNode(val=7),
                                            right=TreeNode(val=2)
                                            )
                              ),
                right=TreeNode(val=8,
                               left=TreeNode(val=13),
                               right=TreeNode(val=4,
                                              right=TreeNode(val=1)
                                              )
                               )
                )
print(Solution().lowestCommonAncestor(root=root, p=TreeNode(val=13), q=TreeNode(val=1)).val)
