# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string."""
        res = []
        q = deque([root])
        while q:
            curr = q.popleft()
            res.append(curr.val if curr else None)
            if curr:
                q.append(curr.left)
                q.append(curr.right)

        # get rid of excess null/None from end
        i = len(res) - 1
        while i >= 0:
            if res[i] is not None:
                break
            i -= 1

        return '#'.join([str(x) for x in res[:i+1]])

    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree."""
        if not data:
            return None

        nodes = [int(node) if node != 'None' else None for node in data.split('#')]
        res = TreeNode(nodes[0])
        
        # iterate through nodes and add to res
        q = deque([res])
        i = 1
        while i < len(nodes):
            curr = q.popleft()
            if nodes[i] is not None:
                curr.left = TreeNode(nodes[i])
                q.append(curr.left)
            i += 1
            if i < len(nodes):
                if nodes[i] is not None:
                    curr.right = TreeNode(nodes[i])
                    q.append(curr.right)
                i += 1

        return res
        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))