"""
给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。
示例：
二叉树：[3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @classmethod
    def levelOrder(cls, root: TreeNode) -> [[int]]:
        if not root:
            return []
        sum = list()
        cache = list()
        cache.append(root)
        while cache:
            subList = list()
            length = len(cache)
            for i in range(0, length):
                node = cache[i]
                subList.append(node.val)
                if node.left:
                    cache.append(node.left)
                if node.right:
                    cache.append(node.right)
            sum.append(subList)
            cache = cache[length:]
        return sum


# [3,9,20,null,null,15,7]
root = TreeNode(val=3, left=TreeNode(val=9), right=TreeNode(val=20, left=TreeNode(val=15), right=TreeNode(val=7)))
print(Solution.levelOrder(root))
