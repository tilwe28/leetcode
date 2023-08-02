class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []
        for p in s:
            if p not in pairs:
                stack.append(p)
            elif stack and stack[-1] == pairs[p]:
                stack.pop()
            else:
                return False
        return not stack
        
"""
STACK
~ iterate through parenthesis
~ use stack and push any open parenthesis
~ when closing parenthesis appears, peak from stack
~ if last element is corresponding opening parenthesis, then pop and continue
~ otherwise return False
"""