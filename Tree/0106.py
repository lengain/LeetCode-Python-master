"""
根据一棵树的中序遍历与后序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

中序遍历 inorder = [9,3,15,20,7]
后序遍历 postorder = [9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        rep = "val=" + str(self.val) + " " + "left="
        if self.left:
            rep += str(self.left)
        else:
            rep += "null"
        rep += " right="
        if self.right:
            rep += str(self.right)
        else:
            rep += "null"
        return rep


"""

中序遍历 inorder = [2,9,6,3,15,20,7]
后序遍历 postorder = [2,6,9,15,7,20,3]
返回如下的二叉树：

    3
   / \
  9   20
 / \  /  \
2   6 15  7
"""


class Solution:
    def buildTree(self, inorder: [int], postorder: [int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        postOrderLength = len(postorder)
        node = TreeNode(val=postorder[postOrderLength - 1])
        index = inorder.index(node.val)
        node.left = self.buildTree(inorder=inorder[:index], postorder=postorder[:index])
        node.right = self.buildTree(inorder=inorder[index + 1:], postorder=postorder[index:postOrderLength-1])
        return node


node = Solution().buildTree(inorder=[9, 3, 15, 20, 7], postorder=[9, 15, 7, 20, 3])
print(node)
