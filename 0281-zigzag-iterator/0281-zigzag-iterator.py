class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        i = 0
        max_len = max(len(v1), len(v2))
        self.iterator = []
        while i < max_len:
            for v in (v1, v2):
                if i < len(v):
                    self.iterator.append(v[i])
            i += 1
        
        self.curr = 0

    def next(self) -> int:
        val = self.iterator[self.curr]
        self.curr += 1
        return val

    def hasNext(self) -> bool:
        return self.curr < len(self.iterator)

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())