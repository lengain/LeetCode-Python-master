"""
根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
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

前序遍历 preorder =[3,9,2,6,20,15,7]
中序遍历 inorder = [2,9,6,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9   20
 / \  /  \
2   6 15  7
"""


class Solution:
    def buildTree(self, preorder: [int], inorder: [int]) -> TreeNode:
        if not preorder or not inorder:
            return None
        node: TreeNode = TreeNode(val=preorder[0])
        index = inorder.index(preorder[0])
        node.left = self.buildTree(preorder=preorder[1:index + 1], inorder=inorder[:index])
        node.right = self.buildTree(preorder=preorder[index + 1:], inorder=inorder[index + 1:])
        return node


node = Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
print(node)
