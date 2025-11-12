class Vector2D:

    def __init__(self, vec: List[List[int]]):
        self.list = []
        for row in vec:
            for v in row:
                self.list.append(v)

        self.curr = 0

    def next(self) -> int:
        val = self.list[self.curr]
        self.curr += 1
        return val

    def hasNext(self) -> bool:
        return self.curr < len(self.list)


# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()