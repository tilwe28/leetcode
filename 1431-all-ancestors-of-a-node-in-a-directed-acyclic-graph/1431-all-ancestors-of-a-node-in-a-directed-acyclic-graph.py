from collections import deque

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        res = []
        edges = sorted([edge[::-1] for edge in edges])
        # edges = list of edges denoting [dest_i, src_i] pairs

        # add initial parents
        for dest, src in edges:
            adj[dest].append(src)

        for i in range(n):
            # BFS
            q = deque(adj[i])
            visited = set(adj[i])
            ancestors = [False] * n

            for parent in adj[i]:
                ancestors[parent] = True

            while q:
                curr = q.popleft()
                for parent in adj[curr]:
                    if parent in visited:
                        continue

                    ancestors[parent] = True
                    q.append(parent)
                    visited.add(parent)
            
            res.append([i for i, ancestor in enumerate(ancestors) if ancestor])
        
        return res

"""
BRUTE FORCE:
- for each node do the following
- check if there are any nodes with an edge to it
- backtrack and check nodes connecting to those

INITIAL THOUGHTS:
- have res list
- reverse and sort edges so that it's list of [dest, src] (ascending order of incoming edges)
- for each node perform BFS
    - find first edge with src as node
    - add to queue
    - 
"""