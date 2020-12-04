"""
请实现两个函数，分别用来序列化和反序列化二叉树。

示例: 

你可以将以下二叉树：

    1
   / \
  2   3
     / \
    4   5

序列化为 "[1,2,3,null,null,4,5]"

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/xu-lie-hua-er-cha-shu-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.desc = '['

        def traverse(node: TreeNode):
            self.desc += str(node.val)
            self.desc += ","
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        self.desc += ']'
        return self.desc

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """


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
print(Codec.serialize(root))
