# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return None
        
        res, q = [], []
        q.append(root)
        while q:
            level = []
            for i in range(len(q)):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(level)
        return res

"""
BINARY TREE
- level order traversal means bfs
- to do bfs use queue to store nodes to visit
- if nodes have child continue to add to queue
- keep going while there are nodes in queue
- each level is defined by nodes in queue at each iteration

- have result list
- have outer while loop that continues as long as there are nodes in queue
- create level list
- have inner for loop that iterates len(queue) amount of times
    - dequeue node and add to level list
    - add nodes children to queue
- add level list to result
"""