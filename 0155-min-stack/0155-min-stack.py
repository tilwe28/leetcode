class MinStack:

    def __init__(self):
        self.stack = deque()
        self.min_stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        min_val = min(val, self.min_stack[-1] if len(self.min_stack) else val)
        self.min_stack.append(min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
"""
idea:
have 2 stacks
first is regular
second always has curr min at top

when pushing element, push to normal stack
also push min(new_val, top(second_stack))
- if new_val < top(second_stack), then it's the new minimum and should be at the top
- else, top(second_stack) is still the minimum and gets pushed again

the reason this duplicate is okay is because when we pop, we pop the new_val from the first
and pop the duplicate from the second
- new_val isn't min and the min cannot be popped off until new_val is popped
- so the actual min isn't popped until enough pops have happened to actually pop it off first
"""

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()