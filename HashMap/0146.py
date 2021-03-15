"""
运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制 。
实现 LRUCache 类：

LRUCache(int capacity) 以正整数作为容量 capacity 初始化 LRU 缓存
int get(int key) 如果关键字 key 存在于缓存中，则返回关键字的值，否则返回 -1 。
void put(int key, int value) 如果关键字已经存在，则变更其数据值；如果关键字不存在，则插入该组「关键字-值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。
 

进阶：你是否可以在 O(1) 时间复杂度内完成这两种操作？

 

示例：

输入
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
输出
[null, null, null, 1, null, -1, null, -1, 3, 4]

解释
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // 缓存是 {1=1}
lRUCache.put(2, 2); // 缓存是 {1=1, 2=2}
lRUCache.get(1);    // 返回 1
lRUCache.put(3, 3); // 该操作会使得关键字 2 作废，缓存是 {1=1, 3=3}
lRUCache.get(2);    // 返回 -1 (未找到)
lRUCache.put(4, 4); // 该操作会使得关键字 1 作废，缓存是 {4=4, 3=3}
lRUCache.get(1);    // 返回 -1 (未找到)
lRUCache.get(3);    // 返回 3
lRUCache.get(4);    // 返回 4
 

提示：

1 <= capacity <= 3000
0 <= key <= 3000
0 <= value <= 104
最多调用 3 * 104 次 get 和 put

作者：力扣 (LeetCode)
链接：https://leetcode-cn.com/leetbook/read/2021-spring-recruitment/5f5qts/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
 """
from collections import OrderedDict


class LRUCache1:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.orderDict = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.orderDict:
            return -1
        self.orderDict.move_to_end()
        return self.orderDict[key]

    def put(self, key: int, value: int) -> None:
        if key in self.orderDict:
            self.orderDict.move_to_end(key)
        self.orderDict[key] = value
        if len(self.orderDict) > self.capacity:
            self.orderDict.popitem(last=False)


class LRUCacheNode:
    def __init__(self, key=0, value=0):
        self.key = key
        self.value = value
        self.pre: LRUCacheNode = None
        self.next: LRUCacheNode = None


class LRUCache:

    def __init__(self, capacity: int):
        self.dic = dict()
        self.head = LRUCacheNode()
        self.tail = LRUCacheNode()
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
        self.size = 0

    def addToHead(self, node: LRUCacheNode):
        node.pre = self.head
        node.next = self.head.next
        self.head.next.pre = node
        self.head.next = node

    def removeNode(self, node: LRUCacheNode):
        node.pre.next = node.next
        node.next.pre = node.pre

    def moveToHead(self, node: LRUCacheNode):
        self.removeNode(node=node)
        self.addToHead(node=node)

    def removeTail(self) -> LRUCacheNode:
        node = self.tail.pre
        self.removeNode(node)
        return node

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        node: LRUCacheNode = self.dic[key]
        self.moveToHead(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return None
        if key not in self.dic:
            if self.capacity == self.size:
                removeNode = self.removeTail()
                self.dic.pop(removeNode.key)
            else:
                self.size += 1
            node = LRUCacheNode(key=key, value=value)
            self.dic[key] = node
            self.addToHead(node)
        else:
            node = self.dic[key]
            node.value = value
            self.moveToHead(node)
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
