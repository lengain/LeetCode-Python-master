"""
112. 路径总和
给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。

说明: 叶子节点是指没有子节点的节点。

示例:
给定如下二叉树，以及目标和 sum = 22，

              5
             / \
            4   8
           /   / \
          11  13  4
         /  \      \
        7    2      1
返回 true, 因为存在目标和为 22 的根节点到叶子节点的路径 5->4->11->2。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if root.val == sum and not root.left and not root.right:
            return True
        self.has = False

        def checkHasPathSum(node: TreeNode, value: int):
            if value == sum and not node.left and not node.right:
                self.has = True
                return
            if node.left:
                checkHasPathSum(node.left, node.left.val + value)
            if node.right:
                checkHasPathSum(node.right, node.right.val + value)

        checkHasPathSum(root, root.val)
        return self.has


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
print(Solution().hasPathSum(root, 22))
