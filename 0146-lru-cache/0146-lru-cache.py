class Node:
    def __init__(self, key, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.head = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # values are nodes

        # head is LRU, tail is MRU
        # two dummy nodes at each end
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    # remove from list but keep cache pointing to it
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    # add to end of list
    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        # update order
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            self.cache[key].val = value
            return
        
        if len(self.cache) < self.capacity:
            self.cache[key] = Node(key, value)
            self.add(self.cache[key])
            return

        # evict LRU
        del self.cache[self.head.next.key]
        self.remove(self.head.next)
        self.cache[key] = Node(key, value)
        self.add(self.cache[key])


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)