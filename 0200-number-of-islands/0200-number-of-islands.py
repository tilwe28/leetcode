from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                # start of island
                if grid[r][c] == '1':
                    num_islands += 1

                    # BFS
                    grid[r][c] = '-'
                    q = deque()
                    q.append((r, c))
                    while q:
                        rn, cn = q.popleft()
                        if rn + 1 < len(grid) and grid[rn + 1][cn] == '1':
                            q.append((rn + 1, cn))
                            grid[rn + 1][cn] = '-'
                        if cn + 1 < len(grid[0]) and grid[rn][cn + 1] == '1':
                            q.append((rn, cn + 1))
                            grid[rn][cn + 1] = '-'
                        if rn - 1 >= 0 and grid[rn - 1][cn] == '1':
                            q.append((rn - 1, cn))
                            grid[rn - 1][cn] = '-'
                        if cn - 1 >= 0 and grid[rn][cn - 1] == '1':
                            q.append((rn, cn - 1))
                            grid[rn][cn - 1] = '-'

        return num_islands