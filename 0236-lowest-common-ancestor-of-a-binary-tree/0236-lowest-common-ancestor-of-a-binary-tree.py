# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_p, path_q = [], []

        def dfs(curr: 'TreeNode', goal: 'TreeNode' , path: List[int]) -> bool:
            if curr == None:
                return False
            if curr.val == goal.val:
                path.append(curr)
                return True
            
            if dfs(curr.left, goal, path) or dfs(curr.right, goal, path):
                path.append(curr)
                return True
            
            return False
        
        dfs(root, p, path_p)
        dfs(root, q, path_q)

        lca = root
        while path_p and path_q:
            p = path_p.pop()
            q = path_q.pop()
            if p == q:
                lca = p
            else:
                break

        return lca

"""
INITIAL THOUGHTS:
- use dfs to find path to nodes
- compare paths, and see any common nodes
- use stack for paths, top is root
- keep popping, last similar is LCA
"""