# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def invert(node):
            if not node:
                return None
            tmp = node.left
            node.left = invert(node.right)
            node.right = invert(tmp)
            return node
        
        return invert(root)

"""
- recursively invert the right and left children of a tree
- do this by having a invert function that switches the children, and returns the root
"""