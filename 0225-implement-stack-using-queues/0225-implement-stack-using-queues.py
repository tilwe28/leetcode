class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.appendleft(x)

    def pop(self) -> int:
        last = self.q[-1]
        tmp = deque()

        while self.q:
            last = self.q.pop()
            if self.q:
                tmp.appendleft(last)

        self.q = tmp
        return last

    def top(self) -> int:
        last = self.q[-1]
        tmp = deque()

        while self.q:
            last = self.q.pop()
            tmp.appendleft(last)

        self.q = tmp
        return last

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()