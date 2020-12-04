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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.desc = '['
        allNodes = [root]
        hasNode = True
        while allNodes and hasNode:
            has = False
            allCount = len(allNodes)
            for i in range(0, allCount):
                item = allNodes[i]
                if isinstance(item, TreeNode):
                    self.desc += str(item.val)
                    if item.left:
                        allNodes.append(item.left)
                        has = True
                    else:
                        allNodes.append(None)
                    if item.right:
                        allNodes.append(item.right)
                        has = True
                    else:
                        allNodes.append(None)
                else:
                    self.desc += 'null'
                self.desc += ','
            if not has:
                descCount = len(self.desc) - 1
                self.desc = self.desc[0:descCount]
            hasNode = has
            allNodes = allNodes[allCount:]

        self.desc += ']'
        return self.desc

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        length = len(data)
        str = data[1:length - 1]
        valList = data.split(",")
        node = TreeNode()
        valCount = len(valList)
        lineCount = 1
        lineTotalCount = 1
        for i in range(0, valCount):
            if i < lineTotalCount:



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
print(Codec().deserialize(Codec().serialize(root)))
