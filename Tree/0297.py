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

    def serialize1(self, root: TreeNode) -> str:
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

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'

        def innerSerialize(node: TreeNode, dec: str) -> str:
            if not node:
                dec += "null,"
            else:
                dec += str(node.val) + ","
                dec = innerSerialize(node.left, dec)
                dec = innerSerialize(node.right, dec)
            return dec

        dec = innerSerialize(node=root, dec="[")
        decLength = len(dec)
        dec = dec[0: decLength - 1]
        dec += "]"
        return dec

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        dataLength = len(data)
        dec = data[1:dataLength - 1]
        if len(dec) == 0:
            return None
        valList: list[str] = dec.split(",")

        def deser(node: TreeNode):
            node.val = valList[0]
            del (valList[0])
            if not valList:
                return
            if valList[0] != 'null':
                node.left = TreeNode()
                deser(node.left)
            else:
                del (valList[0])

            if valList[0] != 'null':
                node.right = TreeNode()
                deser(node.right)
            else:
                del (valList[0])

        node = TreeNode()
        deser(node=node)
        return node


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
# print(Codec().serialize(root))
print(Codec().deserialize(Codec().serialize(None)))
# print(Codec().deserialize(Codec().serialize(root)))
