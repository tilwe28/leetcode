class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        directions = [[1, 0], [0, 1], [-1, 0], [0, -1]] # down, right, up, left

        max_area = 0
        seen = set()

        for i in range(M):
            for j in range(N):
                if grid[i][j] == 1:
                    # BFS
                    q = collections.deque()
                    q.append((i, j))
                    seen.add((i, j))
                    area = 1

                    while q:
                        r, c = q.popleft()

                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (0 <= nr < M and
                                0 <= nc < N and
                                grid[nr][nc] == 1 and
                                (nr, nc) not in seen
                            ):
                                q.append((nr, nc))
                                seen.add((nr, nc))
                                area += 1

                    max_area = max(max_area, area)

                seen.add((i, j))

        return max_area
        
"""
- similar to number of islands
- track max area instead of count

- traverse grid
- when 1 is seen, start BFS
- use seen set of points (avoid repetition)
"""