# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.in_order = []
        
        def traverse(node):
            if not node:
                return
            
            traverse(node.left)
            self.in_order.append(node.val)
            traverse(node.right)
        
        traverse(root)
        self.curr = 0

    def next(self) -> int:
        val = self.in_order[self.curr]
        self.curr += 1
        return val

    def hasNext(self) -> bool:
        return self.curr < len(self.in_order)
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()