# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def height(node):
            if not node:
                return 0
            height_l = height(node.left)
            height_r = height(node.right)
            self.diameter = max(self.diameter, height_l + height_r)
            return max(height_l, height_r) + 1

        height_l = height(root.left)
        height_r = height(root.right)
        self.diameter = max(self.diameter, height_l + height_r)
        return self.diameter