class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()

        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def add(self, node):
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.tail

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        # update LRU order
        self.remove(self.cache[key])
        self.add(self.cache[key])

        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        elif len(self.cache) == self.capacity:
            # remove LRU
            del self.cache[self.head.next.key]
            self.remove(self.head.next)

        self.cache[key] = Node(key, value)
        self.add(self.cache[key])

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
- doubly linked list for storing LRU order and values
- hashmap for storing key to node
"""