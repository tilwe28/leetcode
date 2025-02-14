class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # BFS
        adj = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        initial_color = image[sr][sc]
        if initial_color == color:
            return image

        q = deque()
        q.append((sr, sc))

        while q:
            row, col = q.popleft()
            image[row][col] = color

            for r, c in adj:
                nr, nc = row + r, col + c
                if 0 <= nr and nr < len(image) and 0 <= nc and nc < len(image[0]) and image[nr][nc] == initial_color:
                    q.append((nr, nc))
            
        return image