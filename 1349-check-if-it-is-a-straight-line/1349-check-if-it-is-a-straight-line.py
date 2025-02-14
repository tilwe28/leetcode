class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        # y = mx + b
        # m = (y1 - y0) / (x1 - x0)
        # b = y0 - m*x0
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        if x1 == x0:
            m = float("inf")
        else:
            m = (y1 - y0) / (x1 - x0)
        b = y0 - m*x0

        for x, y in coordinates[2:]:
            if m == float("inf"):
                if x != x0:
                    return False
            elif y != m*x + b:
                return False

        return True