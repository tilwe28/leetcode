class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i, row in enumerate(grid):
            for j, val in enumerate(row):
                if val == '1':
                    count += 1
                    stack = []
                    stack.append((i, j))
                    while stack:
                        r, c = stack.pop()
                        grid[r][c] = 'x'
                        if r > 0 and grid[r - 1][c] == '1':
                            stack.append((r - 1, c))
                        if r + 1 < len(grid) and grid[r + 1][c] == '1':
                            stack.append((r + 1, c))
                        if c > 0 and grid[r][c - 1] == '1':
                            stack.append((r, c - 1))
                        if c + 1 < len(row) and grid[r][c + 1] == '1':
                            stack.append((r, c + 1))
        return count

"""
- iterate through grid
- if a 1 is spotten, increment the count and run bfs
- during dfs, mark all 1s in island as 'x'
"""