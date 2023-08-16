# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # recursive dfs

"""
BINARY TREE
- traverse to maximum depth and count each step down
- to achieve this, add 1 to max(depth(left), depth(right))
- if there is no left or right return none
NOTE: many tree problems can be solved easily with recursion as the tree can be broken down into subtrees with  
      the same properties. this way the base cases are more easily seen.
"""