"""
给定一个二叉树，检查它是否是镜像对称的。

 

例如，二叉树 [1,2,2,3,4,4,3] 是对称的。

    1
   / \
  2   2
 / \ / \
3  4 4  3
 

但是下面这个 [1,2,2,null,3,null,3] 则不是镜像对称的:

    1
   / \
  2   2
   \   \
   3    3


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 递归法
class Solution:
    @classmethod
    def isSymmetric(cls, root: TreeNode) -> bool:
        def check(p: TreeNode, q: TreeNode) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return p.val == q.val and check(p.left, q.right) and check(p.right, q.left)

        return check(root, root)


# 迭代法
class Solution2:
    @classmethod
    def isSymmetric(cls, root: TreeNode) -> bool:
        if not root:
            return True
        queue = [root.left, root.right]
        while queue:
            left = queue.pop(0)
            right = queue.pop(0)
            if not right and left:
                return False
            if not left and right:
                return False
            if not right and not left:
                continue
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True


# [1,2,2,null,3,null,3]
root = TreeNode(val=1, left=TreeNode(val=2, right=TreeNode(val=3)),
                right=TreeNode(val=2, right=TreeNode(val=3)))
print(Solution.isSymmetric(root))
print(Solution2.isSymmetric(root))
