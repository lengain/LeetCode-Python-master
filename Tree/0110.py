"""
给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：
一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。

解析：首先有个子函数能够获取二叉树的深度，
    然后保证当前根节点和左右子树的高度都不超过1就行了

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def isBalanced(cls, root: TreeNode) -> bool:

        def height(sub_root: TreeNode) -> int:
            if not sub_root:
                return 0
            return max(height(sub_root.left), height(sub_root.right)) + 1

        if not root:
            return True
        return abs(height(root.left) - height(root.right)) <= 1
        Solution.isBalanced(root.left) and Solution.isBalanced(
            root.right)
