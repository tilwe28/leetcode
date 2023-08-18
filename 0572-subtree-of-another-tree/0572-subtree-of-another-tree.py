# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val and self.isSameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

"""
BINARY TREE
- continuation of same tree
- go through root until node.val == subRoot.val
- then call isSameTree from that position
    - if returns True, then isSubtree returns True
    - otherwise keep traversing through root
- if isSameTree always returns false or is never called, return False

- create isSameTree function
- do a recursive dfs on root and call isSameTree whenever node.val == subRoot.val
"""